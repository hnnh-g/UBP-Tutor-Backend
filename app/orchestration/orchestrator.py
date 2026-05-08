from app.orchestration.models import OrchestrationRequest, OrchestrationResponse
from app.orchestration.task_router import TaskRouter


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
