from app.rag.document_loader import DocumentLoader
from app.rag.text_splitter import TextSplitter


def main():
    loader = DocumentLoader()
    documents = loader.load_documents()

    splitter = TextSplitter()
    chunks = splitter.split_documents(documents)

    print(f"Total Chunks: {len(chunks)}")
    print("\nFirst Chunk:\n")
    print(chunks[0].page_content)


if __name__ == "__main__":
    main()