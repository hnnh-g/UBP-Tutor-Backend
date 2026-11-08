from app.schemas.chat import TaskType
from app.orchestration.workflows import (
    TextTutoringWorkflow,
    ModelGenerationWorkflow,
    ModelEvaluationWorkflow,
)

class TaskRouter:
    def __init__(self):
        self.workflows = {
            TaskType.TEXT_TUTORING: TextTutoringWorkflow(),
            TaskType.SUMMARY: TextTutoringWorkflow(),
            TaskType.QUESTION_GENERATION: TextTutoringWorkflow(),
            TaskType.MODEL_EVALUATION: ModelEvaluationWorkflow(),
            TaskType.MODEL_GENERATION: ModelGenerationWorkflow(),
            TaskType.ANSWER_EVALUATION: TextTutoringWorkflow(),
            
        }

    def route(self, task_type: TaskType):
        workflow = self.workflows.get(task_type)

        if workflow is None:
            raise ValueError(f"Unsupported task type: {task_type}")
        
        return workflow
