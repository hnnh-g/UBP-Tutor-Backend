from app.llm.litellm_client import LiteLLMClient
from app.prompts.text_tutoring_prompt import TEXT_TUTORING_SYSTEM_PROMPT


class TextTutoringAgent:
    def __init__(self):
        self.llm = LiteLLMClient(
        model="gpt-4o-mini",
        temperature=0.0,        
        )

    def build_response(self, message: str, rag_context: str | None = None,) -> list[dict]:
        context = rag_context or "No retrieved context was provided."

        return [
            {
                "role": "system",
                "content": TEXT_TUTORING_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"""
                Retrieved context: {context}
                Student question: {message}
                """,
            },
        ]

    async def generate_response(self, message: str, user_context, metadata: dict, rag_context: str | None = None) -> str:
        messages = self.build_response(
            message=message,
            rag_context=rag_context,
        )
        return await self.llm.generate(messages)

    async def stream_response(self, message: str, user_context=None, metadata: dict | None = None, rag_context: str | None = None):
        
        messages = self.build_response(
            message=message,
            rag_context=rag_context,
        )

        async for token in self.llm.stream(messages):
            yield token