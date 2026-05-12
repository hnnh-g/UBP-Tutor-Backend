from google.adk.agents import LlmAgent, SequentialAgent, LoopAgent
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from app.prompts.model_generation_prompt import MODEL_GENERATION_SYSTEM_PROMPT
from app.syntax_checker.syntax_tool import validate_model_syntax

def validate_and_exit_if_valid(model_text: str, tool_context):
    result = validate_model_syntax(model_text)
    if result["valid"]:
        tool_context.actions.escalate = True
    return result

class ModelGenerationAgent:
    def __init__(self):
        self.app_name = "ubp_tutor"

        # 1 defines agent (mode and behavior)
        model_generation_agent = LlmAgent(
            name="model_generation_agent",
            model=LiteLlm(model="openai/gpt-4o-mini"),
            instruction=MODEL_GENERATION_SYSTEM_PROMPT,
            generate_content_config=types.GenerateContentConfig(
                temperature=0.0
            ),
            tools=[validate_and_exit_if_valid]
        )

        # 2 define Loop Agent 
        generation_loop = LoopAgent(
            name="model_generation_refinement",
            sub_agents=[model_generation_agent],
            max_iterations=3
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

    def build_prompt(self, message: str, rag_context: str | None = None) -> str:
        return f"""
        Retrieved RAG context: {rag_context or "No retrieved context provided."}
        Student question: {message}
        """
    
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

    async def generate_response(self, message: str, user_context, metadata: dict | None = None, rag_context: str | None = None) -> str:
        user_id = getattr(user_context, "sub", "anonym")
        session_id = (
            metadata.get("session:id")
            if metadata and metadata.get("session_id")
            else "default"
        )

        await self.ensure_session(user_id, session_id)
        prompt = self.build_prompt(message, rag_context)

        # create structured message object
        adk_message = types.Content(
            role="user",
            parts=[types.Part(text=prompt)]
        )
        final_text = ""

        # Execution (run agent insides this session with the provided input)
        async for event in self.runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=adk_message
        ):
            # extract text from event
            if event.is_final_response() and event.content and event.content.parts:
                final_text = ""
                for part in event.content.parts:
                    if part.text:
                        final_text += part.text
        
        return final_text