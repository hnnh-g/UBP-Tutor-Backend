import nltk
import numpy as np

class SemanticChunker:

    def __init__(self, similarity_threshold: float = 0.85, max_sentences_per_chunk: int = 5):
        self.similarity_threshold = similarity_threshold
        self.max_sentences_per_chunk = max_sentences_per_chunk

    def _cosine_similarity(self, a: list[float], b: list[float]) -> float:
        a, b = np.array(a), np.array(b)
        return float(np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b)))

    async def chunk(self, text:str, embed_fn) -> list[str]:
        sentences = nltk.sent_tokenize(text)
        if len(sentences) <= 1:
            return sentences
        
        embeddings = await embed_fn(sentences)

        chunks = []
        current_chunk = [sentences[0]]

        for i in range(1, len(sentences)):
            similarity = self._cosine_similarity(embeddings[i-1], embeddings[i])
            # create new chunk if similarity is too low or the chunk is already too large
            if similarity < self.similarity_threshold or len(current_chunk) >= self.max_sentences_per_chunk: 
                chunks.append(" ".join(current_chunk))
                current_chunk = [sentences[i]]
            else:
                # append sentence to the current chunk
                current_chunk.append(sentences[i])
        
        # close chunk 
        chunks.append(" ".join(current_chunk))
        # return all chunks
        return chunks
