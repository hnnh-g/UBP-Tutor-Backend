import httpx
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)

class Reranker:
    def __init__(self, top_n: int = 2):
        self.url = f"{settings.vllm_reranker_url}/rerank"
        self.model = "vllm-reranker-model"
        self.top_n = top_n

    _MODEL_MAX_TOKENS = 8192
    _OVERHEAD_TOKENS = 400  # prompt template overhead
    _CHARS_PER_TOKEN = 3    # conservative estimate for German text

    def _max_chars_per_doc(self, query: str, n_docs: int) -> int:
        query_tokens = len(query) // self._CHARS_PER_TOKEN + 1
        available = self._MODEL_MAX_TOKENS - self._OVERHEAD_TOKENS - query_tokens
        return max(100, (available // n_docs) * self._CHARS_PER_TOKEN)

    async def rerank(self, query: str, documents: list[str]) -> list[str]:
        if not documents:
            return []

        max_chars = self._max_chars_per_doc(query, len(documents))
        truncated = [doc[:max_chars] for doc in documents]


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
