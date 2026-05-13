from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.status import AdminUserResponse
from app.services.keycloak_admin_service import KeycloakAdminService
from app.core.security import get_current_user
from app.schemas.user import UserContext

router = APIRouter(tags=["Admin"])
admin_service = KeycloakAdminService()

# check if users has admin role before getting admin information (role-based access)
def require_admin(user: UserContext = Depends(get_current_user)) -> UserContext:
    if "ADMIN" not in user.roles:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return user

@router.get("/admin/users", response_model=AdminUserResponse)
async def get_users_overview(user: UserContext = Depends(require_admin)):
    return await admin_service.get_users_overview()
