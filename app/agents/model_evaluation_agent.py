import asyncio


class ModelEvaluationAgent:
    async def generate_model(self, message):
        return f"Generated model based on: {message}"

    async def stream_model_generation(self, message):
        tokens = ["Generating ", "model ", "step ", "by ", "step..."]
        for token in tokens:
            await asyncio.sleep(0.1)
            yield token

from google.adk.agents import Agent

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

root_agent = Agent(
    model='gemini-flash-latest',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)