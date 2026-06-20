"""
RAGAs evaluation script for all three tutor agents.

Usage (run from backend/ directory):
    python -m app.rag.eval.eval_rag text_tutor
    python -m app.rag.eval.eval_rag model_eval
    python -m app.rag.eval.eval_rag model_gen

Requires:
    pip install ragas datasets
    OPENAI_API_KEY=...
"""

import asyncio
import sys
import os
import logging
import importlib
from app.agents.text_tutoring_agent import TextTutoringAgent
from app.agents.model_evaluation_agent import ModelEvaluationAgent
from app.agents.model_generation_agent import ModelGenerationAgent
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI

evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini"))

logging.basicConfig(level=logging.WARNING)

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import faithfulness, context_precision, context_recall

from app.rag.retriever import Retriever

# configuration and mapping for each agent 
AGENTS = {
    "text_tutor": {
        "tutor_name": "text_tutor",
        "dataset_module": "app.rag.eval.dataset_text_tutor",
        "streaming": True,
    },
    "model_eval": {
        "tutor_name": "model_evaluation_tutor",
        "dataset_module": "app.rag.eval.dataset_model_eval",
        "streaming": True,
    },
    "model_gen": {
        "tutor_name": "model_generation_tutor",
        "dataset_module": "app.rag.eval.dataset_model_gen",
        "streaming": False,
    },
}

# helper to run response generation
async def get_answer_streaming(agent, message: str, contexts: list[str]) -> str:
    tokens = []
    async for token in agent.stream_response(
        message=message,
        user_context=None, # none to fake the user that calls the model
        rag_context="\n\n".join(contexts),
    ):
        tokens.append(token)
    return "".join(tokens)


async def get_answer_blocking(agent, message: str, contexts: list[str]) -> str:
    return await agent.generate_response(
        message=message,
        user_context=None,
        rag_context="\n\n".join(contexts),
    )

async def run_pipeline(agent_key: str) -> None:
    config = AGENTS[agent_key]
    mod = importlib.import_module(config["dataset_module"])
    dataset = mod.dataset
    retriever = Retriever(config["tutor_name"])

    if agent_key == "text_tutor":
        agent = TextTutoringAgent()
    elif agent_key == "model_eval":
        agent = ModelEvaluationAgent()
    else:
        agent = ModelGenerationAgent()

    rows = []
    for i, row in enumerate(dataset):
        print(f"[{i+1}/{len(dataset)}] {row['question'][:70]}...")

        # get retrieved chunks as a list[str] -> required by RAGAs
        contexts = await retriever.retrieve_as_list(row["question"])

        if config["streaming"]:
            answer = await get_answer_streaming(agent, row["question"], contexts)
        else:
            answer = await get_answer_blocking(agent, row["question"], contexts)

        rows.append({
            "question": row["question"],
            "answer": answer,
            "contexts": contexts,
            "ground_truth": row["ground_truth"],
        })

    print(f"\nRunning RAGAs evaluation for '{agent_key}'...")
    ragas_dataset = Dataset.from_list(rows)

    # calls RAGAs evaluate to receive the results for the metrics
    results = evaluate(
        ragas_dataset,
        metrics=[faithfulness, context_precision, context_recall],
        llm=evaluator_llm,
    )

    print("\n--- Results ---")
    print(results)

    # saves produced results
    output_path = os.path.join(os.path.dirname(__file__), f"results_{agent_key}.csv")
    results.to_pandas().to_csv(output_path, index=False)
    print(f"\nSaved to {output_path}")

# entry point for the code that executes the code
if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in AGENTS:
        print(f"Usage: python -m app.rag.eval.eval_rag [{' | '.join(AGENTS)}]")
        sys.exit(1)

    asyncio.run(run_pipeline(sys.argv[1]))
