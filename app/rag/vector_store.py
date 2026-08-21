from pathlib import Path

import faiss
import numpy as np
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS


class VectorStore:

    def __init__(self):
        self.index_path = Path("knowledge_base/vector_store")

    def create(self, embeddings, documents, embedding_model):
        dimension = embeddings.shape[1]

        index = faiss.IndexFlatL2(dimension)

        vector_store = FAISS(
            embedding_function=embedding_model.embed_query,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )

        vector_store.add_embeddings(
            text_embeddings=[
                (doc.page_content, emb)
                for doc, emb in zip(documents, embeddings)
            ],
            metadatas=[
                doc.metadata
                for doc in documents
            ],
        )

        self.index_path.mkdir(parents=True, exist_ok=True)

        vector_store.save_local(str(self.index_path))

        print("Vector Store created successfully.")

        return vector_store

    def load(self, embedding_model):
        return FAISS.load_local(
            str(self.index_path),
            embedding_model.embed_query,
            allow_dangerous_deserialization=True,
        )