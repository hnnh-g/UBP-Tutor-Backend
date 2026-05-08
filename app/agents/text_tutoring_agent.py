import asyncio


class TextTutoringAgent:
    async def generate_response(self, message, user_context, metadata):
        return f"Text tutoring response for: {message}"

    async def stream_response(self, message):
        tokens = ["This ", "is ", "a ", "streamed ", "tutoring ", "response."]
        for token in tokens:
            await asyncio.sleep(0.1)
            yield token