"""
RAGAs evaluation script for all three tutor agents.

Calls the vLLM servers directly (bypassing the google ADK framework) to avoid
the ~14k-token orchestration overhead that would exceed the 15k context limit.

Usage (run from backend/ directory):
    python -m app.rag.eval.eval_rag text_tutor
    python -m app.rag.eval.eval_rag model_eval
    python -m app.rag.eval.eval_rag model_gen

Requires:
    pip install ragas datasets openai
    OPENAI_API_KEY=...  (for the RAGAs evaluator LLM)
"""

import asyncio
import sys
import os
import logging
import importlib
from openai import AsyncOpenAI
from langchain_openai import ChatOpenAI
from ragas.llms import LangchainLLMWrapper

evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o-mini", max_tokens=2048))

logging.basicConfig(level=logging.WARNING)

from datasets import Dataset
from ragas import evaluate
from ragas.metrics._faithfulness import faithfulness
from ragas.metrics._context_precision import context_precision
from ragas.metrics._context_recall import context_recall

from app.rag.retriever import Retriever
from app.core.config import settings
from app.prompts.text_tutoring_prompt import TEXT_TUTORING_SYSTEM_PROMPT
from app.prompts.model_evaluation_prompt import MODEL_EVALUATION_SYSTEM_PROMPT
from app.prompts.model_generation_prompt import MODEL_GENERATION_SYSTEM_PROMPT

# per-agent vLLM endpoint + system prompt config
AGENTS = {
    "text_tutor": {
        "tutor_name": "text_tutor",
        "dataset_module": "app.rag.eval.dataset_text_tutor",
        "api_base": settings.vllm_text_tutor_url,
        "model": "text-tutor",
        "system_prompt": TEXT_TUTORING_SYSTEM_PROMPT,
    },
    "model_eval": {
        "tutor_name": "model_evaluation_tutor",
        "dataset_module": "app.rag.eval.dataset_model_eval",
        "api_base": settings.vllm_model_evaluation_url,
        "model": "model-evaluation",
        "system_prompt": MODEL_EVALUATION_SYSTEM_PROMPT,
    },
    "model_gen": {
        "tutor_name": "model_generation_tutor",
        "dataset_module": "app.rag.eval.dataset_model_gen",
        "api_base": settings.vllm_model_generation_url,
        "model": "model-generation",
        "system_prompt": MODEL_GENERATION_SYSTEM_PROMPT,
    },
}


def _build_user_message(message: str, contexts: list[str]) -> str:
    rag_context = "\n\n".join(contexts)
    return f"Retrieved RAG context: {rag_context}\n\nStudent question: {message}"


async def get_answer(client: AsyncOpenAI, config: dict, message: str, contexts: list[str]) -> str:
    response = await client.chat.completions.create(
        model=config["model"],
        messages=[
            {"role": "system", "content": config["system_prompt"]},
            {"role": "user", "content": _build_user_message(message, contexts)},
        ],
        temperature=0.1,
        extra_body={"repetition_penalty": 1.1},
    )
    return response.choices[0].message.content or ""


async def run_pipeline(agent_key: str) -> None:
    config = AGENTS[agent_key]
    mod = importlib.import_module(config["dataset_module"])
    dataset = mod.dataset
    retriever = Retriever(config["tutor_name"])

    client = AsyncOpenAI(base_url=config["api_base"], api_key="EMPTY")

    rows = []
    for i, row in enumerate(dataset):
        print(f"[{i+1}/{len(dataset)}] {row['question'][:70]}...")

        contexts = await retriever.retrieve_as_list(row["question"])
        answer = await get_answer(client, config, row["question"], contexts)

        rows.append({
            "question": row["question"],
            "answer": answer,
            "contexts": contexts,
            "ground_truth": row["ground_truth"],
        })

    print(f"\nRunning RAGAs evaluation for '{agent_key}'...")
    ragas_dataset = Dataset.from_list(rows)

    results = evaluate(
        ragas_dataset,
        metrics=[faithfulness, context_precision, context_recall],
        llm=evaluator_llm,
    )

    print("\n--- Results ---")
    print(results)

    # saves produced results
    output_path = os.path.join(os.path.dirname(__file__), f"results2_{agent_key}.csv")
    results.to_pandas().to_csv(output_path, index=False)
    print(f"\nSaved to {output_path}")

# entry point for the code that executes the code
if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in AGENTS:
        print(f"Usage: python -m app.rag.eval.eval_rag [{' | '.join(AGENTS)}]")
        sys.exit(1)

    asyncio.run(run_pipeline(sys.argv[1]))
