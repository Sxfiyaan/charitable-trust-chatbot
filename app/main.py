from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.rag.knowledge_base_watcher import KnowledgeBaseWatcher
from app.routers.chat import router as chat_router


watcher = KnowledgeBaseWatcher()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start knowledge base watcher
    watcher.start_background()

    yield

    # Stop watcher when FastAPI shuts down
    watcher.stop()


app = FastAPI(
    title="Charitable Trust AI Chatbot",
    description="AI-powered chatbot for the Charitable Trust website",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "Charitable Trust AI Chatbot API is running."
    }