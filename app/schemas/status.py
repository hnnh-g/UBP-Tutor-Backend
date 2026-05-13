from pydantic import BaseModel
from typing import Literal, Dict, Optional

class ComponentHealth(BaseModel):
    reachable: bool
    detail: Optional[str] = None

class AgentInfo(BaseModel):
    name: str
    task_types: list[str]

class HealthResponse(BaseModel):
    status: Literal["healthy", "degraded", "unhealthy"]
    components: Dict[str, ComponentHealth]

class StatusResponse(BaseModel):
    active_model: Optional[str] = None
    active_requests: int
    streaming_active: bool
    available_agents: list[AgentInfo]
    components: Dict[str, ComponentHealth]

class UserAdminInfo(BaseModel):
    id: str
    username: str
    email: Optional[str] = None
    roles: list[str]
    enabled: bool # check if account is active
    last_login: Optional[str] = None

class AdminUserResponse(BaseModel):
    total_users: int
    active_sessions: int
    roles_distribution: Dict[str, int]
    users: list[UserAdminInfo]




