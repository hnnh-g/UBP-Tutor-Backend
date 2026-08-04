import logging
import uuid
from google.adk.agents import LlmAgent, SequentialAgent, LoopAgent
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from app.prompts.model_generation_prompt import MODEL_GENERATION_SYSTEM_PROMPT
from app.syntax_checker.syntax_tool import validate_model_syntax
from app.syntax_checker.extractors.bpmn_extractor import strip_bpmndi
from app.core.config import settings

logger = logging.getLogger(__name__)

MAX_VALIDATION_ATTEMPTS = 2

# NOTE: the syntax check is deliberately NOT exposed as an LLM tool.

class ModelGenerationAgent:
    def __init__(self):
        self.app_name = "ubp_tutor"

        # 1 defines agent (mode and behavior)
        model_generation_agent = LlmAgent(
            name="model_generation_agent",
            model=LiteLlm(
                model="openai/model-generation",
                api_base=settings.vllm_model_generation_url,
                api_key="EMPTY",
                extra_body={"stop": ["</s>"]},
            ),
            instruction=MODEL_GENERATION_SYSTEM_PROMPT,
            generate_content_config=types.GenerateContentConfig(
                temperature=0.1
            )
        )

        # 2 define Loop Agent 
        generation_loop = LoopAgent(
            name="model_generation_refinement",
            sub_agents=[model_generation_agent],
            max_iterations=1
        )

        # 3 define Sequential Agent (to add other agents / tools easier later as well)
        self.adk_agent = SequentialAgent(
            name="model_generation_pipeline",
            sub_agents=[generation_loop],
            description="Executes a sequence of model generation task."
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

    def build_prompt(self, message: str, rag_context: str | None = None, correction: str | None = None) -> str:
        # Mirrors the fine-tuning format:
        BPMN_DIRECTIVE = "Create a BPMN process diagram."
        directive = BPMN_DIRECTIVE if "bpmn" in message.lower() else message.strip()
        parts = [directive, "", "### Input:", message.strip()]
        if rag_context:
            parts += ["", f"Retrieved RAG context (follow its syntax patterns and reuse its domain names where they apply): {rag_context}"]
        if correction:
            parts += ["", correction]
        return "\n".join(parts)
    
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

    async def generate_response(self, message: str, user_context, session_id: str, metadata: dict | None = None, rag_context: str | None = None) -> str:
        user_id = getattr(user_context, "sub", "anonym")
        await self.ensure_session(user_id, session_id)

        base_prompt = self.build_prompt(message, rag_context)
        prompt = base_prompt
        last_text = ""

        for attempt in range(1, MAX_VALIDATION_ATTEMPTS + 1):
            # a fresh session per attempt keeps each retry independent
            session_id = str(uuid.uuid4())
            await self.ensure_session(user_id, session_id)

            adk_message = types.Content(
                role="user",
                parts=[types.Part(text=prompt)]
            )

            # collect the model's text output - this is the diagram itself
            text = ""
            try:
                async for event in self.runner.run_async(
                    user_id=user_id,
                    session_id=session_id,
                    new_message=adk_message
                ):
                    if event.content and event.content.parts:
                        for part in event.content.parts:
                            if part.text:
                                text += part.text
            except ValueError as e:
                logger.warning("Runner raised ValueError: %s", e)

            last_text = text.strip()
            result = validate_model_syntax(strip_bpmndi(last_text))
            logger.info(
                "Validation attempt %d/%d: valid=%s (model length: %d chars)",
                attempt, MAX_VALIDATION_ATTEMPTS, result.get("valid"), len(last_text)
            )

            if result.get("valid"):
                logger.info("Model generation succeeded (%d chars)", len(last_text))
                return last_text

            # feed the syntax errors back so the next attempt can correct itself
            correction = "\n".join([
                "The previous attempt was invalid.",
                f"syntax error: {result.get('issues')}",
                f"previous attempt: {last_text}",
                "Please correct the diagram.",
            ])
            prompt = self.build_prompt(message, rag_context, correction=correction)

        logger.warning(
            "Model generation produced no valid model after %d attempt(s)",
            MAX_VALIDATION_ATTEMPTS
        )
        return last_text