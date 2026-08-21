from app.rag.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "What is Agentic RAG?"
)

print(f"Retrieved {len(results)} documents\n")

for i, doc in enumerate(results, start=1):
    print("=" * 70)
    print(f"Chunk {i}")
    print("=" * 70)
    print(doc.page_content)
    print()