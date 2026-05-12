from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat
from app.routers import user
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="UBP Tutor Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api")
app.include_router(chat.router, prefix="/api")


@app.get("/api/health")
async def health():
    return {
        "status": "ok",
        "components": {
            "api": "reachable",
            "orchestration": "reachable",
        },
    }
