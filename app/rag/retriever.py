from app.rag.chroma_client import get_collection
from app.rag.embedder import Embedder
from app.rag.reranker import Reranker
import logging

logger = logging.getLogger(__name__)

class Retriever:

    def __init__(self, tutor_name: str, n_documents: int = 10, n_results: int = 2):
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
            include=["documents", "distances"],
        )

        candidates = results["documents"][0]
        distances = results["distances"][0]
        logger.info(f"Retrieved {len(candidates)} candidates for tutor '{self.tutor_name}' | query: '{query[:60]}'")
        for i, (doc, dist) in enumerate(zip(candidates, distances)):
            logger.info(f"  Chunk {i+1} (dist={dist:.4f}): {doc[:150]}...")

        results = await self.reranker.rerank(query, candidates)
        for i, chunk in enumerate(results):
            logger.info(f"  Final chunk {i+1}: {chunk[:150]}...")
        return "\n\n".join(results)
    
    async def retrieve_as_list(self, query: str) -> list[str]:
        query_embedding = await self.embedder.embed_query(query)
        collection = get_collection(self.tutor_name)
        results = collection.query(query_embeddings=[query_embedding], n_results=self.n_documents, include=["documents"])
        candidates = results["documents"][0]
        return await self.reranker.rerank(query, candidates)  # already returns a list

