from openai import OpenAI
from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url=PORTKEY_GATEWAY_URL,
    default_headers=createHeaders(
        provider="openai",
        api_key=os.environ.get("PORTKEY_API_KEY")
    )
)
# , "content": "You are an Agent."
def get_completion(prompt, temperature=0):
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature
        )
    
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    total_tokens = prompt_tokens + completion_tokens

    print("input token count: ", prompt_tokens)
    print("response token count: ", completion_tokens)
    print("total tokens: ", total_tokens)
    return response.choices[0].message.content.strip()