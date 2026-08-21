from app.rag.document_loader import DocumentLoader
from app.rag.text_splitter import TextSplitter
from app.rag.embedding_service import EmbeddingService
from app.rag.vector_store import VectorStore


class KnowledgeBaseIndexer:

    def __init__(self):
        self.document_loader = DocumentLoader()
        self.text_splitter = TextSplitter()
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def build(self):
        print("=" * 60)
        print("Starting Knowledge Base Indexing")
        print("=" * 60)

        # 1. Load documents
        documents = self.document_loader.load_documents()

        if not documents:
            print("No documents found. Indexing stopped.")
            return

        # 2. Split documents into chunks
        chunks = self.text_splitter.split_documents(documents)

        if not chunks:
            print("No chunks created. Indexing stopped.")
            return

        # 3. Generate embeddings
        embeddings = self.embedding_service.embed_documents(chunks)

        print(f"Generated embeddings: {embeddings.shape}")

        # 4. Create / replace FAISS vector store
        self.vector_store.create(
            embeddings=embeddings,
            documents=chunks,
            embedding_model=self.embedding_service,
        )

        print("=" * 60)
        print("Knowledge Base Indexing Completed")
        print("=" * 60)