from app.rag.document_loader import DocumentLoader
from app.rag.text_splitter import TextSplitter
from app.rag.embedding_service import EmbeddingService
from app.rag.vector_store import VectorStore


loader = DocumentLoader()
documents = loader.load_documents()

splitter = TextSplitter()
chunks = splitter.split_documents(documents)

embedder = EmbeddingService()
embeddings = embedder.embed_documents(chunks)

store = VectorStore()
store.create(
    embeddings=embeddings,
    documents=chunks,
    embedding_model=embedder,
)