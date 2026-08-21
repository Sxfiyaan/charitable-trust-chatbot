from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from app.rag.knowledge_base_indexer import KnowledgeBaseIndexer


class KnowledgeBaseEventHandler(FileSystemEventHandler):

    def __init__(self):
        self.indexer = KnowledgeBaseIndexer()

    def _is_supported_file(self, path):
        return Path(path).suffix.lower() in {".pdf", ".docx"}

    def on_created(self, event):
        if event.is_directory:
            return

        if self._is_supported_file(event.src_path):
            print(f"\nNew document detected: {event.src_path}")
            self.indexer.build()

    def on_modified(self, event):
        if event.is_directory:
            return

        if self._is_supported_file(event.src_path):
            print(f"\nDocument modified: {event.src_path}")
            self.indexer.build()

    def on_deleted(self, event):
        if event.is_directory:
            return

        if self._is_supported_file(event.src_path):
            print(f"\nDocument deleted: {event.src_path}")
            self.indexer.build()


class KnowledgeBaseWatcher:

    def __init__(self, documents_path="knowledge_base/documents"):
        self.documents_path = Path(documents_path)
        self.observer = None

    def start_background(self):

        if not self.documents_path.exists():
            raise FileNotFoundError(
                f"Documents directory not found: {self.documents_path}"
            )

        event_handler = KnowledgeBaseEventHandler()

        self.observer = Observer()

        self.observer.schedule(
            event_handler,
            str(self.documents_path),
            recursive=False,
        )

        self.observer.start()

        print("=" * 60)
        print("Knowledge Base Watcher Started")
        print(f"Watching: {self.documents_path}")
        print("Supported files: PDF, DOCX")
        print("=" * 60)

    def stop(self):

        if self.observer:
            self.observer.stop()
            self.observer.join()

            print("Knowledge Base Watcher Stopped.")