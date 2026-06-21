from app.rag.chroma_client import get_collection
from app.rag.embedder import Embedder
from app.rag.chunkers.paragraph_chunker import ParagraphChunker
from app.rag.chunkers.semantic_chunker import SemanticChunker
from pathlib import Path 
import logging
logger = logging.getLogger(__name__)

DOCUMENTS_DIR = Path(__file__).parent / "documents"


# mapping each tutor to its chunking strategy
TUTOR_CONFIG = {
    "text_tutor":             {"chunking": "semantic",  "separator": "\n\n", "paragraphs_per_chunk": 1},
    "model_evaluation_tutor": {"chunking": "paragraph", "separator": "---",  "paragraphs_per_chunk": 1},
    "model_generation_tutor": {"chunking": "paragraph", "separator": "---",  "paragraphs_per_chunk": 3},
}


class Ingestion:

    def __init__(self):
        self.embedder = Embedder()
        self.paragraph_chunker = ParagraphChunker()
        self.semantic_chunker = SemanticChunker()

    async def ingest_all_documents(self) -> None:
        for tutor_name, config in TUTOR_CONFIG.items():
            folder = DOCUMENTS_DIR / tutor_name
            if not folder.exists():
                continue

            collection = get_collection(tutor_name)

            for file_path in folder.glob("*.md"):
                logger.info(f"Processing {file_path.name} for '{tutor_name}'...")
                existing = collection.get(ids=[f"{file_path.name}_0"])
                if existing["ids"]:
                    logger.info(f"Skipping {file_path.name} — already ingested")
                    continue

                text = file_path.read_text(encoding="utf-8")
                count = await self.ingest(
                    text=text,
                    tutor_name=tutor_name,
                    source=file_path.name,
                    chunking=config["chunking"],
                    separator=config["separator"],
                    paragraphs_per_chunk=config.get("paragraphs_per_chunk", 1),
                )
                logger.info(f"Ingested {file_path.name} → {count} chunks into '{tutor_name}'")


    async def ingest(self, text: str, tutor_name: str, source: str, chunking: str = "paragraph", separator: str = "\n\n", paragraphs_per_chunk: int = 1) -> int:
        if chunking == "semantic":
            chunks = await self.semantic_chunker.chunk(text, self.embedder.embed)
        else:
            chunker = ParagraphChunker(separator=separator, paragraphs_per_chunk=paragraphs_per_chunk)
            chunks = chunker.chunk(text)

        # create embeddings for the created chunks
        embeddings = await self.embedder.embed(chunks)

        # create collection according to the tutor
        collection = get_collection(tutor_name)
        ids = [f"{source}_{i}" for i in range(len(chunks))]

        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=chunks,
            metadatas=[{"source": source, "chunk_index": i} for i in range(len(chunks))],
        )

        return len(chunks)

