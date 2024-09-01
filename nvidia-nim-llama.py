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
  messages=[{"role":"user","content":"How can i find the LLM models' limits on NVIDIA NIM?"}],
  temperature=0.8,
  top_p=0.7,
  max_tokens=50000,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

