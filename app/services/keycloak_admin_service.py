import httpx
from app.core.config import settings
from app.schemas.status import UserAdminInfo, AdminUserResponse
from collections import Counter

class KeycloakAdminService:

    # private only internal helper
    async def _get_admin_token(self) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{settings.keycloak_url}/realms/master/protocol/openid-connect/token",
                data={
                    "grant_type": "password",
                    "client_id": "admin-cli",
                    "username": settings.keycloak_admin_user,
                    "password": settings.keycloak_admin_password
                }
            )
            response.raise_for_status()
            return response.json()["access_token"]
        
    async def get_users_overview(self) -> AdminUserResponse:
        token = await self._get_admin_token()
        headers = {"Authorization": f"Bearer {token}"}
        base = f"{settings.keycloak_url}/admin/realms/{settings.keycloak_realm}"

        async with httpx.AsyncClient() as client:
            # fetch all users
            users_response = await client.get(f"{base}/users", headers=headers)
            users_response.raise_for_status()
            users_data = users_response.json()

            users = []
            for user in users_data:
                user_id = user["id"]

                # fetch realm roles for this user
                roles_response = await client.get(
                f"{base}/users/{user_id}/role-mappings",
                headers=headers)
                roles_response.raise_for_status()
                mapping = roles_response.json()

                # realm roles
                realm_roles = [r["name"] for r in mapping.get("realmMapping", [])]

                #client roles
                client_roles = []
                for client_mapping in mapping.get("clientMappings", {}).values():
                    client_roles += [r["name"] for r in client_mapping.get("mappings", [])]

                roles = realm_roles + client_roles

                # get last login for user
                last_login_ms = user.get("lastLogin")  
                last_login = str(last_login_ms) if last_login_ms else None

                users.append(UserAdminInfo(
                    id=user_id,
                    username=user.get("username", ""),
                    email=user.get("email"),
                    roles=roles,
                    enabled=user.get("enabled", False),
                    last_login=last_login,
                ))

            # get session data
            sessions_response = await client.get(f"{base}/client-session-stats", headers=headers)
            sessions_response.raise_for_status()
            sessions_data = sessions_response.json()

            active_sessions = next(
                (int(s.get("active", 0)) 
                for s in sessions_data 
                if s.get("clientId") == "ubp-frontend"),
                0
            )

            # count role occurrence
            roles_distribution = dict(Counter(role for u in users for role in u.roles))    

            return AdminUserResponse(
                total_users=len(users_data),
                active_sessions=active_sessions,
                roles_distribution=roles_distribution,
                users=users
            )