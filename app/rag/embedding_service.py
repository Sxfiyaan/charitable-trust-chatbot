from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self, model_name="BAAI/bge-small-en-v1.5"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, documents):
        texts = [doc.page_content for doc in documents]
        embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True,
        )
        return embeddings

    def embed_query(self, query: str):
        return self.model.encode(
            query,
            convert_to_numpy=True,
        )