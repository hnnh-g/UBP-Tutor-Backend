from app.schemas.status import HealthResponse, ComponentHealth, StatusResponse, AgentInfo
from sqlalchemy import text
from app.database.database import engine
from app.core.config import settings

# module level counter (for ongoing processes)
active_requests: int = 0

def increment_requests():
    global active_requests
    active_requests += 1

def decrement_requests():
    global active_requests
    active_requests -=1

class MonitorService: 
    async def get_health(self) -> HealthResponse:
        # check if database connection can be established by letting it return 1
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            db_health = ComponentHealth(reachable=True)

        except Exception as e:
            db_health = ComponentHealth(reachable=False, detail=str(e))

        # include all components (DB, vLLM, Chroma DB)
        components = {
            "database": db_health
        }

        values = components.values()

        if all(c.reachable for c in values):
            overall = "healthy"
        elif any(c.reachable for c in values):
            overall = "degraded"
        else: 
            overall = "unhealthy"

        return HealthResponse(status=overall, components=components)
    
    async def get_status(self) -> StatusResponse:
        health = await self.get_health()
        active_model = settings.active_model

        available_agents = [
            AgentInfo(name="TextTutoringAgent", task_types=["question", "summary", "question_generation", "answer_evaluation"]),
            AgentInfo(name="ModelGenerationAgent", task_types=["model_generation"]),
            AgentInfo(name="ModelEvaluationAgent", task_types=["model_evaluation"])
        ]

        return StatusResponse(
            active_model=active_model,
            active_requests=active_requests,
            streaming_active=True,
            available_agents=available_agents,
            components=health.components
        )