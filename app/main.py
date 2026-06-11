from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.rag.ingestion import Ingestion
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat
from app.routers import user
from app.routers import status
from app.routers import admin
import logging

logging.basicConfig(level=logging.INFO)

@asynccontextmanager
async def lifespan(app):
    await Ingestion().ingest_all_documents()
    yield

app = FastAPI(title="UBP Tutor Backend", lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(status.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
