import chromadb
from app.core.config import settings

client = chromadb.HttpClient(
    host=settings.chroma_host,
    port=settings.chroma_port
)

def get_collection(tutor_name: str):
    return client.get_or_create_collection(
        name=tutor_name,
        configuration={"hnsw": {"space": "cosine"}},
    )

