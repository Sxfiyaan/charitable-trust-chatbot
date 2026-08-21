import json

from app.core.redis import redis_client


class RedisMemoryRepository:
    def __init__(self):
        self.redis = redis_client

    def _get_key(self, session_id: str) -> str:
        return f"chat:{session_id}"

    def add_message(self, session_id: str, role: str, content: str):
        message = {
            "role": role,
            "content": content
        }

        # Store the message
        self.redis.rpush(
            self._get_key(session_id),
            json.dumps(message)
        )

        # Keep only the last 16 messages
        self.redis.ltrim(
            self._get_key(session_id),
            -16,
            -1
        )

        # Refresh expiry to 48 hours
        self.redis.expire(
            self._get_key(session_id),
            48 * 60 * 60
        )

    def get_history(self, session_id: str):
        messages = self.redis.lrange(
            self._get_key(session_id),
            0,
            -1
        )

        return [json.loads(message) for message in messages]

    def clear_history(self, session_id: str):
        self.redis.delete(self._get_key(session_id))