import httpx
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class Reranker:
    def __init__(self, top_n: int = 2):
        self.url = f"{settings.vllm_reranker_url}/rerank"
        self.model = "vllm-reranker-model"
        self.top_n = top_n

    _MAX_CHARS_PER_DOC = 1000

    async def rerank(self, query: str, documents: list[str]) -> list[str]:
        if not documents:
            return []
        
        truncated = [doc[: self._MAX_CHARS_PER_DOC] for doc in documents]


        try:
            async with httpx.AsyncClient(timeout=60.0) as http:
                response = await http.post(
                    self.url,
                    json={
                        "model": self.model,
                        "query": query,
                        "documents": truncated,
                        "top_n": self.top_n,
                    },
                )
                if not response.is_success:
                    logger.error(f"Reranker returned {response.status_code}: {response.text}")
                    return documents[: self.top_n]
                data = response.json()

            results = sorted(data["results"], key=lambda x: x["relevance_score"], reverse=True)
            logger.info(
                f"Reranked {len(documents)} → {len(results[:self.top_n])} chunks"
                f" | top score: {results[0]['relevance_score']:.3f}"
            )
            return [documents[r["index"]] for r in results[: self.top_n]]

        except Exception as e:
            logger.error(f"Reranker failed, returning top-{self.top_n} by embedding score: {e}")
            return documents[: self.top_n]
