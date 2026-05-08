from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.security import get_current_user
from app.schemas.user import UserPreferences, UserPreferencesUpdate
import app.services.user_service as user_service

router = APIRouter(tags=["User"])


@router.get("/user/preferences", response_model=UserPreferences)
def read_user_preferences(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return user_service.get_user_preferences(db, current_user)


@router.patch("/user/preferences", response_model=UserPreferences)
def patch_user_preferences(
    data: UserPreferencesUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return user_service.update_user_preferences(db, current_user, data)
