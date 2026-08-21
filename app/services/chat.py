import os
import time

from dotenv import load_dotenv

from app.core.ai_client import client
from app.services.prompt_service import PromptService
from app.services.conversation_service import ConversationService
from app.services.rag_service import RAGService

load_dotenv()

MODEL = os.getenv("GROQ_MODEL")


class ChatService:

    @staticmethod
    def get_response(session_id: str, user_message: str) -> str:

        system_prompt = PromptService.get_system_prompt()

        ConversationService.add_user_message(
            session_id,
            user_message
        )

        history = ConversationService.get_history(session_id)

        rag_context = RAGService.get_context(user_message)

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        messages.extend(history)

        if rag_context:
            messages.append(
        {
            "role": "system",
            "content": (
                "Use the following retrieved knowledge base information "
                "to answer the user's question. "
                "If the answer is not present in the context, clearly say you don't know.\n\n"
                f"{rag_context}"
            )
        }
    )

        start = time.perf_counter()

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.3
        )

        end = time.perf_counter()

        print("=" * 60)
        print(f"LLM Response Time : {end - start:.2f} seconds")
        print("=" * 60)

        ai_response = response.choices[0].message.content

        ConversationService.add_assistant_message(
            session_id,
            ai_response
        )

        return ai_response