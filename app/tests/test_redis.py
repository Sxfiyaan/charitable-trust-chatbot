from app.core.redis import redis_client

# Save data
redis_client.set("name", "sufiyaan")

# Read data
value = redis_client.get("name")

print(value)