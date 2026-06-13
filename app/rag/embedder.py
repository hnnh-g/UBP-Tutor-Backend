import httpx
from app.core.config import settings

class Embedder:
    def __init__(self):
        self.url = f"{settings.vllm_embedding_url}/embeddings"
        self.model = "vllm-embedding-model"

    async def embed(self, texts: list[str]) -> list[list[float]]:
        async with httpx.AsyncClient(timeout=120.0) as http:
            response = await http.post(
                self.url,
                json={
                    "model": self.model,
                    "input": [f"passage: {t}" for t in texts],
                    "truncate_prompt_tokens": 512,
                },
            )
            response.raise_for_status()
            data = response.json()
            return [item["embedding"] for item in data["data"]]
        
    async def embed_query(self, query: str) -> list[float]:
        instruction = "Instruct: Given a student question, retrieve relevant material.\nQuery: "
        async with httpx.AsyncClient(timeout=120.0) as http:
            response = await http.post(
                self.url,
                json={
                    "model": self.model,
                    "input": [f"{instruction}{query}"],
                    "truncate_prompt_tokens": 512,
                },
            )
            response.raise_for_status()
            data = response.json()
            return data["data"][0]["embedding"]