from sqlalchemy.orm import Session

from app.database.models import UserPreference
from app.schemas.user import UserPreferencesUpdate


def _get_or_create(db: Session, current_user: dict) -> UserPreference:
    # if no user entry exits create one at first login and set to default preferences
    user = (
        db.query(UserPreference)
        .filter(UserPreference.keycloak_user_id == current_user["sub"])
        .first()
    )

    if not user:
        user = UserPreference(
            keycloak_user_id=current_user["sub"],
            email=current_user.get("email"),
            username=current_user.get("preferred_username"),
            # language, theme, default_task_type fall back to the column defaults
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    return user


def get_user_preferences(db: Session, current_user: dict) -> UserPreference:
    return _get_or_create(db, current_user)


def update_user_preferences(
    db: Session, current_user: dict, preferences: UserPreferencesUpdate
) -> UserPreference:
    user = _get_or_create(db, current_user)

    # Only update fields the client actually sent
    update_data = preferences.model_dump(exclude_unset=True)

    field_map = {"defaultTaskType": "default_task_type"}
    for field, value in update_data.items():
        column = field_map.get(field, field)
        setattr(user, column, value)

    db.commit()
    db.refresh(user)
    return user
