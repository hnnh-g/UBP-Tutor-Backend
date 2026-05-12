from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from app.prompts.text_tutoring_prompt import TEXT_TUTORING_SYSTEM_PROMPT

class TextTutoringAgent:
    def __init__(self):
        self.app_name = "ubp_tutor"

        # 1 defines agent (mode and behavior)
        tutor_agent = LlmAgent(
            name="text_tutoring_agent",
            model=LiteLlm(model="openai/gpt-4o-mini"),
            instruction=TEXT_TUTORING_SYSTEM_PROMPT,
            generate_content_config=types.GenerateContentConfig(
                temperature=0.0
            )
        )

        # 2 define sequential agent for deterministic workflow
        self.adk_agent = SequentialAgent(
            name="text_tutoring_pipeline",
            sub_agents=[tutor_agent],
            description="Executes a sequence of text tutoring task including RAG retrieval and generating an answer."
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

    async def stream_response(self, message: str, user_context, metadata: dict | None = None, rag_context: str | None = None):
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

        # Execution (run agent insides this session with the provided input)
        async for event in self.runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=adk_message,
            run_config=RunConfig(streaming_mode=StreamingMode.SSE),
        ):
            # extract text from event
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        # text immediately send to frontend
                        yield part.text