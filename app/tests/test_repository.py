from app.repositories.redis_memory_repository import RedisMemoryRepository

repo = RedisMemoryRepository()

repo.clear_history("test")

history = repo.get_history("test")

print(history)