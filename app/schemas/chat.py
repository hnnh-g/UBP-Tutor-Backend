from enum import Enum 
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class TaskType(str, Enum):
    TEXT_TUTORING = "question"
    MODEL_GENERATION = "model_generation"
    MODEL_EVALUATION = "model_evaluation"
    SUMMARY = "summary"
    QUESTION_GENERATION = "question_generation"
    ANWER_EVALUATION = "answer_evaluation"

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    task_type: TaskType
    session_id: Optional[str] = None
    metadata: Dict[str, Any] = {}

class ChatResponse(BaseModel):
    content: str
    activate_agent: str
    status: str
    rag_used: bool