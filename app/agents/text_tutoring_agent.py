from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from app.prompts.text_tutoring_prompt import TEXT_TUTORING_SYSTEM_PROMPT
from app.core.config import settings

class TextTutoringAgent:
    def __init__(self):
        self.app_name = "ubp_tutor"

        # 1 defines agent (mode and behavior)
        tutor_agent = LlmAgent(
            name="text_tutoring_agent",
            model=LiteLlm(
                model="openai/text-tutor",
                api_base=settings.vllm_text_tutor_url,
                api_key="EMPTY",
                extra_body={"repetition_penalty": 1.1, "stop": ["</s>"]},
            ),
            instruction=TEXT_TUTORING_SYSTEM_PROMPT,
            generate_content_config=types.GenerateContentConfig(
                temperature=0.1,
            )
        )

        # 2 define sequential agent for deterministic workflow
        self.adk_agent = SequentialAgent(
            name="text_tutoring_pipeline",
            sub_agents=[tutor_agent],
            description="Executes a sequence of text tutoring task."
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

    def build_prompt(self, message: str) -> str:
        return "\n".join([
            message.strip(),
            "",
        ])
    
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

    async def stream_response(self, message: str, user_context, session_id: str, metadata: dict | None = None):
        user_id = getattr(user_context, "sub", "anonym")
        await self.ensure_session(user_id, session_id)
        prompt = self.build_prompt(message)

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
            # Only yield partial streaming events from the inner LLM agent.
            # The SequentialAgent wrapper also emits a final event with the full
            # accumulated content, which would cause the response to appear twice.
            if event.author == "text_tutoring_agent" and event.partial and event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        yield part.text