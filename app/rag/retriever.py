from app.rag.chroma_client import get_collection
from app.rag.embedder import Embedder
import logging

logger = logging.getLogger(__name__)

class Retriever:

    def __init__(self, tutor_name: str, n_results: int = 5):
        self.tutor_name = tutor_name
        self.n_results = n_results
        self.embedder = Embedder()

    async def retrieve(self, query: str) -> str:
        query_embedding = await self.embedder.embed_query(query)
        collection = get_collection(self.tutor_name)

        # query collection to find chunks with similar context
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=self.n_results,
        )

        documents = results["documents"][0]

        # debug log to see if it worked
        logger.info(f"Retrieved {len(documents)} chunks for tutor '{self.tutor_name}' | query: '{query[:60]}'")

        return "\n\n".join(documents)
