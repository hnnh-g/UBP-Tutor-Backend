from pydantic import BaseModel
from typing import Literal, Optional, List

class SyntaxIssue(BaseModel):
    severity: Literal["error", "warning"]
    code: str
    message: str
    element_id: Optional[str] = None
    location: Optional[str] = None
    suggestions: Optional[str] = None

class SyntaxValidationResult(BaseModel):
    valid: bool
    notation: Literal["uml", "bpmn", "pnml", "unknown"]
    parser: str
    issues: List[SyntaxIssue]