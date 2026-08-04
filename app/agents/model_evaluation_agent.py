import logging
from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from app.prompts.model_evaluation_prompt import MODEL_EVALUATION_SYSTEM_PROMPT
from app.syntax_checker.syntax_tool import validate_model_syntax
from app.syntax_checker.extractors.bpmn_extractor import strip_bpmndi
from app.core.config import settings

logger = logging.getLogger(__name__)

class ModelEvaluationAgent:
    def __init__(self):
        self.app_name = "ubp_tutor"

        # 1 defines agent (mode and behavior)
        evaluator_agent = LlmAgent(
            name="model_evaluation_agent",
            model=LiteLlm(
                model="openai/model-evaluation",
                api_base=settings.vllm_model_evaluation_url,
                api_key="EMPTY",
                extra_body={"repetition_penalty": 1.1, "stop": ["</s>"]},
            ),
            instruction=MODEL_EVALUATION_SYSTEM_PROMPT,
            generate_content_config=types.GenerateContentConfig(
                temperature=0.1,
            ),
        )

        # 2 define sequential agent for deterministic workflow
        self.adk_agent = SequentialAgent(
            name="model_evaluation_pipeline",
            sub_agents=[evaluator_agent],
            description="Executes a sequence of diagram evaluation tasks."
        )

        # stores adk session (used to remember and organize interactions)
        # TODO: replace with database-backend session for persistence
        self.session_service = InMemorySessionService()

        # executes agent
        self.runner = Runner(
            agent=self.adk_agent,
            app_name=self.app_name,
            session_service=self.session_service,
        )

    def build_prompt(self, message: str, rag_context: str | None = None) -> str:
        # The prompt mirrors the fine-tuning format:
        logger.info("Running syntax check on student model (%d chars)", len(message))
        syntax_result = validate_model_syntax(message)
        model_for_llm = strip_bpmndi(message).strip()

        # every training example had a fenced code block as input
        if not model_for_llm.startswith("```"):
            model_for_llm = f"```\n{model_for_llm}\n```"

        rag_line = (
            f"Retrieved RAG context: {rag_context}\n"
            if rag_context and rag_context.strip() else ""
        )

        return (
            "Evaluate the following diagram. Identify modeling errors and give suggestions in how to improve the diagram.\n"
            "\n"
            f"Syntax check (additional Information): {syntax_result}\n"
            f"{rag_line}"
            "\n"
            "### Input:\n"
            f"{model_for_llm}"
        )
    
    # create conversation session for tutor and student
    async def ensure_session(self, user_id: str, session_id: str) -> None:
        try:
            await self.session_service.create_session(
                app_name=self.app_name,
                user_id=user_id,
                session_id=session_id
            )
        except Exception:
            # TODO: handle session that already exists
            pass

    async def stream_response(self, message: str, user_context,session_id: str, metadata: dict | None = None, rag_context: str | None = None):
        user_id = getattr(user_context, "sub", "anonym")
        user_id = getattr(user_context, "sub", "anonym")
        await self.ensure_session(user_id, session_id)
        prompt = self.build_prompt(message, rag_context)

        # create structured message object
        adk_message = types.Content(
            role="user",
            parts=[types.Part(text=prompt)]
        )

        # Execution (run agent insides this session with the provided input)
        async for event in self.runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=adk_message,
            run_config=RunConfig(streaming_mode=StreamingMode.SSE),
        ):
            if event.author == "model_evaluation_agent" and event.partial and event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        yield part.text