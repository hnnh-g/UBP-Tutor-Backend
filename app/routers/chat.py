import json
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest, ChatResponse
from app.schemas.user import UserContext
from app.core.security import get_current_user
from app.orchestration.orchestrator import Orchestrator
from app.orchestration.models import OrchestrationRequest
from app.services.monitoring_service import increment_requests, decrement_requests

router = APIRouter(tags=["Chat"])

orchestrator = Orchestrator()

@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    user_context: UserContext = Depends(get_current_user),
):
    increment_requests()
    try: 
        internal_request = OrchestrationRequest(
            message=request.message,
            task_type=request.task_type,
            session_id=request.session_id,
            metadata=request.metadata,
            user_context=user_context
        )
        result = await orchestrator.process(internal_request)

        return ChatResponse(
            content=result.content,
            activate_agent=result.activated_agent,
            status=result.status,
            rag_used=result.rag_used,
        )
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    
    finally: 
        decrement_requests()
    
@router.post("/chat/stream")
async def chat_stream(
    request: ChatRequest,
    user_context: UserContext = Depends(get_current_user),
):
    internal_request = OrchestrationRequest(
        message=request.message,
        task_type=request.task_type,
        session_id=request.session_id,
        metadata=request.metadata,
        user_context=user_context,
    )

    async def event_generator():
        increment_requests()
        try:
            async for event in orchestrator.stream_process(internal_request):
                yield f"data: {json.dumps(event)}\n\n"

            yield f"data: {json.dumps({'event': 'done', 'status': 'success'})}\n\n"

        except Exception as e:
            error_event = {
                "event": "error",
                "status": "failed",
                "message": str(e),
            }
            yield f"data: {json.dumps(error_event)}\n\n"

        finally:
            decrement_requests()

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
    )