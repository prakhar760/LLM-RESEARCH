from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NVIDIA_NIM_KEY")

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = api_key
)

completion = client.chat.completions.create(
  model="meta/llama-3.1-70b-instruct",
  messages=[{"role":"user","content":"Tell me your model name and model version?"}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=10024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

