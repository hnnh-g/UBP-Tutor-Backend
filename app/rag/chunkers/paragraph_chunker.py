class ParagraphChunker: 

    def __init__(self, paragraphs_per_chunk: int = 2,  separator: str = "\n\n"):
        self.paragraphs_per_chunk = paragraphs_per_chunk
        self.separator = separator

    def chunk(self, text: str) -> list[str]:
        paragraphs = [p.strip() for p in text.split(self.separator) if p.strip()]

        chunks = []
        for i in range(0, len(paragraphs), self.paragraphs_per_chunk):
            group = paragraphs[i : i + self.paragraphs_per_chunk]
            chunks.append(self.separator.join(group))
        return chunks
