from app.orchestration.models import OrchestrationResponse
from app.agents.text_tutoring_agent import TextTutoringAgent
from app.agents.model_generation_agent import ModelGenerationAgent
from app.agents.model_evaluation_agent import ModelEvaluationAgent

class TextTutoringWorkflow:
    def __init__(self):
        self.agent = TextTutoringAgent()
    
    async def stream(self, request):
        async for token in self.agent.stream_response(
            message=request.message,
            user_context=request.user_context,
            metadata=request.metadata,
        ):
            yield {
                "event": "token",
                "data": token,
                "activated_agent": "TextTutoringAgent",
                "rag_used": True,
            }

class ModelGenerationWorkflow:
    def __init__(self):
        self.agent = ModelGenerationAgent()

    async def run(self, request):
        content = await self.agent.generate_response(message=request.message,
            user_context=request.user_context,
            metadata=request.metadata,)

        return OrchestrationResponse(
            content=content,
            activated_agent="ModelGenerationAgent",
            status="success",
            rag_used=False,
        )


class ModelEvaluationWorkflow:
    def __init__(self):
        self.agent = ModelEvaluationAgent()

    async def stream(self, request):
        async for token in self.agent.stream_response(message=request.message,
            user_context=request.user_context,
            metadata=request.metadata,):
            yield {
                "event": "token",
                "data": token,
                "activated_agent": "ModelEvaluationAgent",
                "rag_used": False,
            }