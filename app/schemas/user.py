from typing import Literal
from pydantic import BaseModel, Field, ConfigDict


class UserPreferences(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    language: Literal["de", "en"]
    theme: Literal["light", "dark"]
    # validation_alias maps the snake_case DB column to the camelCase JSON field name
    defaultTaskType: Literal[
        "generation", "evaluation", "question", "summary", "QAgeneration", "chat"
    ] = Field(validation_alias="default_task_type")


class UserPreferencesUpdate(BaseModel):
    language: Literal["de", "en"] | None = None
    theme: Literal["light", "dark"] | None = None
    defaultTaskType: Literal[
        "generation", "evaluation", "question", "summary", "QAgeneration", "chat"
    ] | None = None
