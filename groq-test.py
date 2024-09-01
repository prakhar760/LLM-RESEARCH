import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


api_key=os.getenv("GROQ2_API_KEY")
client = Groq(
    api_key=api_key
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Tell me the top 2 changes happening in the world.",
        }
    ],
    model="llama-3.1-70b-versatile",
    max_tokens=8000
)
prompt_tokens = chat_completion.usage.prompt_tokens
completion_tokens = chat_completion.usage.completion_tokens
total_tokens = prompt_tokens + completion_tokens
print("Thing1: ", prompt_tokens)
print("Thing2: ", completion_tokens)
print("Thing3: ", total_tokens)

print(chat_completion.choices[0].message.content)