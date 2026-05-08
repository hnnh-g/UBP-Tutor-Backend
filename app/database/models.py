from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.sql import func
from app.database.database import Base


class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    keycloak_user_id = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(255))
    email = Column(String(255))
    language = Column(String(10), default="en", nullable=False)
    theme = Column(String(50), default="light", nullable=False)
    default_task_type = Column(String(100), default="question", nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
