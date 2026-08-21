from app.rag.retriever import Retriever


class RAGService:

    _retriever = Retriever()

    @classmethod
    def get_context(cls, user_query: str) -> str:
        documents = cls._retriever.retrieve(
            query=user_query,
            k=3
        )

        if not documents:
            return ""

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        return context