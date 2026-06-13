from app.rag.chroma_client import get_collection
from app.rag.embedder import Embedder
from app.rag.reranker import Reranker
import logging

logger = logging.getLogger(__name__)

class Retriever:

    def __init__(self, tutor_name: str, n_documents: int = 5, n_results: int = 2):
        self.tutor_name = tutor_name
        self.n_documents = n_documents
        self.n_results = n_results
        self.embedder = Embedder()
        self.reranker = Reranker(top_n=n_results)

    async def retrieve(self, query: str) -> str:
        query_embedding = await self.embedder.embed_query(query)
        collection = get_collection(self.tutor_name)

        # query collection to find chunks with similar context
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=self.n_documents,
            include=["documents"],
        )

        candidates = results["documents"][0]
        logger.info(f"Retrieved {len(candidates)} candidates for tutor '{self.tutor_name}' | query: '{query[:60]}'")
        for i, doc in enumerate(candidates):
            logger.info(f"  Chunk {i+1}: {doc[:150]}...")

        results = await self.reranker.rerank(query, candidates)
        return "\n\n".join(results)
