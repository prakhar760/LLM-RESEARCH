import requests
import json
from dotenv import load_dotenv
import os
from fireworks.client import Fireworks

load_dotenv()

api_key = os.getenv("FIREWORKSAI_API_KEY")

client = Fireworks(api_key=api_key)

response = client.chat.completions.create(
    model="accounts/fireworks/models/llama-v3p1-405b-instruct",
    messages=[
        {
            "role": "user",
            "content": "Hi",
        }
    ],
)

prompt_tokens = response.usage.prompt_tokens
completion_tokens = response.usage.completion_tokens
total_tokens = prompt_tokens + completion_tokens
print("Thing1: ", prompt_tokens)
print("Thing2: ", completion_tokens)
print("Thing3: ", total_tokens)

print(response.choices[0].message.content)
