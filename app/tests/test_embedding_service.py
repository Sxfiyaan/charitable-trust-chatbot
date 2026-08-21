from app.rag.document_loader import DocumentLoader
from app.rag.text_splitter import TextSplitter
from app.rag.embedding_service import EmbeddingService


loader = DocumentLoader()
documents = loader.load_documents()

splitter = TextSplitter()
chunks = splitter.split_documents(documents)

embedder = EmbeddingService()
embeddings = embedder.embed_documents(chunks)

print(f"Embeddings Shape: {embeddings.shape}")
print(f"First Vector Length: {len(embeddings[0])}")