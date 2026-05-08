import asyncio


class ModelGenerationAgent:
    async def generate_model(self, message):
        return f"Generated model based on: {message}"

    async def stream_model_generation(self, message):
        tokens = ["Generating ", "model ", "step ", "by ", "step..."]
        for token in tokens:
            await asyncio.sleep(0.1)
            yield token