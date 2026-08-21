import time
import requests

start = time.time()

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "qwen3.5:4b",
        "messages": [
            {
                "role": "user",
                "content": "Hello"
            }
        ],
        "stream": False
    }
)

print(response.json()["message"]["content"])

print(f"\nTime Taken: {time.time() - start:.2f} seconds")