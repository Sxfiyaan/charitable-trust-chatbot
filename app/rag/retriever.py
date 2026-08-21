from app.rag.embedding_service import EmbeddingService
from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store_manager = VectorStore()

        self.reload()

    def reload(self):
        self.vector_store = self.vector_store_manager.load(
            self.embedding_service
        )

        print("Retriever reloaded successfully.")

    def retrieve(self, query: str, k: int = 3):
        return self.vector_store.similarity_search(
            query=query,
            k=k,
        )