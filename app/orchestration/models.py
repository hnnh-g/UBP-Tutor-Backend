from pydantic import BaseModel
from typing import Dict, Any, Optional
from app.schemas.chat import TaskType
from app.schemas.user import UserContext


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
