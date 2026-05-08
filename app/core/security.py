import time
import requests as http
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.schemas.user import UserContext

from app.core.config import settings

security = HTTPBearer()

# Simple in-memory cache so we don't hit Keycloak on every request and refresh every hour
_jwks_cache: dict = {"data": None, "fetched_at": 0.0}
_CACHE_TTL = 3600


def _get_jwks() -> dict:
    now = time.monotonic()
    if _jwks_cache["data"] is None or now - _jwks_cache["fetched_at"] > _CACHE_TTL:
        url = (
            f"{settings.keycloak_url}/realms/{settings.keycloak_realm}"
            "/protocol/openid-connect/certs"
        )
        response = http.get(url, timeout=10)
        response.raise_for_status()
        _jwks_cache["data"] = response.json()
        _jwks_cache["fetched_at"] = now
    return _jwks_cache["data"]


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> UserContext:
    token = credentials.credentials
    try:
        jwks = _get_jwks()
        payload = jwt.decode(
            token,
            jwks,
            algorithms=["RS256"],
            options={"verify_aud": False},
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is missing subject claim",
        )

    # Extract roles
    roles = (payload.get("realm_access", {}).get("roles", []))

    return UserContext(
        sub=user_id,
        email=payload.get("email"),
        preferred_username=payload.get("preferred_username"),
        roles=roles
    )
