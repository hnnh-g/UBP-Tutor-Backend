from app.orchestration.models import OrchestrationResponse
from app.agents.text_tutoring_agent import TextTutoringAgent
from app.agents.model_generation_agent import ModelGenerationAgent
from app.agents.model_evaluation_agent import ModelEvaluationAgent
from app.rag.retriever import Retriever

class TextTutoringWorkflow:
    def __init__(self):
        self.agent = TextTutoringAgent()
        self.retriever = Retriever("text_tutor")
    
    async def stream(self, request):
        rag_context = await self.retriever.retrieve(request.message)
        async for token in self.agent.stream_response(
            message=request.message,
            user_context=request.user_context,
            metadata=request.metadata,
            rag_context=rag_context
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
        self.retriever = Retriever("model_generation")

    async def run(self, request):
        rag_context = await self.retriever.retrieve(request.message)
        content = await self.agent.generate_response(message=request.message,
            user_context=request.user_context,
            metadata=request.metadata, rag_context=rag_context)

        return OrchestrationResponse(
            content=content,
            activated_agent="ModelGenerationAgent",
            status="success",
            rag_used=True,
        )


class ModelEvaluationWorkflow:
    def __init__(self):
        self.agent = ModelEvaluationAgent()
        self.retriever = Retriever("model_evaluation")

    async def stream(self, request):
        rag_context = await self.retriever.retrieve(request.message)
        async for token in self.agent.stream_response(message=request.message,
            user_context=request.user_context,
            metadata=request.metadata,rag_context=rag_context):
            yield {
                "event": "token",
                "data": token,
                "activated_agent": "ModelEvaluationAgent",
                "rag_used": True,
            }