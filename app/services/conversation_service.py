from app.repositories.redis_memory_repository import RedisMemoryRepository


class ConversationService:

    repository = RedisMemoryRepository()

    @classmethod
    def get_history(cls, session_id: str):
        return cls.repository.get_history(session_id)

    @classmethod
    def add_user_message(cls, session_id: str, message: str):
        cls.repository.add_message(
            session_id=session_id,
            role="user",
            content=message
        )

    @classmethod
    def add_assistant_message(cls, session_id: str, message: str):
        cls.repository.add_message(
            session_id=session_id,
            role="assistant",
            content=message
        )

    @classmethod
    def clear_history(cls, session_id: str):
        cls.repository.clear_history(session_id)