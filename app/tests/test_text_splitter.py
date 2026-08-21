from app.rag.document_loader import DocumentLoader
from app.rag.text_splitter import TextSplitter


loader = DocumentLoader()
documents = loader.load_documents()

splitter = TextSplitter()
chunks = splitter.split_documents(documents)

print(f"First chunk:\n\n{chunks[0].page_content}")