from pydantic import BaseModel
from typing import Dict, Any, Optional
from schemas.chat import TaskType
from schemas.user import UserContext
from orchestration.task_router import TaskRouter

class OrchestrationRequest(BaseModel):
    message: str
    task_type: TaskType
    user_context: UserContext
    session_id: Optional[str] = None
    metadata: Dict[str, Any] = {}


class OrchestrationResponse(BaseModel):
    content: str
    activated_agent: str
    status: str
    rag_used: bool

class Orchestrator: 
    def __init__(self):
        self.task_router = TaskRouter()

    async def process(self, request: OrchestrationRequest) -> OrchestrationResponse:
        workflow = self.task_router.route(request.task_type)
        result = await workflow.run(request)
        return result
    
    async def stream_process(self, request: OrchestrationRequest):
        workflow = self.task_router.route(request.task_type)

        async for event in workflow.stream(request):
            yield event