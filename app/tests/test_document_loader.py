from app.rag.document_loader import DocumentLoader

loader = DocumentLoader()

documents = loader.load_documents()

print(f"\nTotal pages loaded: {len(documents)}\n")

if documents:
    print("First page preview:\n")
    print(documents[0].page_content[:500])
    print("\nMetadata:")
    print(documents[0].metadata)