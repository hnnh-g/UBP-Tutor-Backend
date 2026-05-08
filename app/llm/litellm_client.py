from litellm import acompletion
from typing import AsyncGenerator

class LiteLLMClient:
    def __init__(
            self,
            model: str,
            temperature: float = 0.0,
    ):
        self.model = model
        self.temperature = temperature

    async def generate(self, message: list[dict]) -> str:
        response = await acompletion(
            model=self.model,
            messages=message,
            temperature=self.temperature,
        )
        
        return response["choices"][0]["message"]["content"]
    
    async def stream(self, message: list[dict]) -> AsyncGenerator[str, None]:
        response = await acompletion(
            model=self.model,
            messages=message,
            temperature=self.temperature,
            stream=True,
        )

        async for chunk in response:
            delta = chunk["choices"][0]["delta"].get("content")
            if delta: 
                yield delta
