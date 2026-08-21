from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
)


class DocumentLoader:

    def __init__(self, documents_path="knowledge_base/documents"):
        self.documents_path = Path(documents_path)

    def load_documents(self):

        if not self.documents_path.exists():
            raise FileNotFoundError(
                f"Documents directory not found: {self.documents_path}"
            )

        documents = []

        # Load PDF files
        for pdf_file in self.documents_path.glob("*.pdf"):
            print(f"Loading PDF: {pdf_file.name}")

            loader = PyPDFLoader(str(pdf_file))
            documents.extend(loader.load())

        # Load DOCX files
        for docx_file in self.documents_path.glob("*.docx"):
            print(f"Loading DOCX: {docx_file.name}")

            loader = Docx2txtLoader(str(docx_file))
            documents.extend(loader.load())

        if not documents:
            print("Warning: No PDF or DOCX documents found.")

        print(f"Loaded {len(documents)} document pages.")

        return documents