from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HF_KEY")

client = OpenAI(
	api_key=api_key,
	base_url="https://huggingface.co/api/integrations/dgx/v1",
)
response = client.chat.completions.create(
	model="meta-llama/Meta-Llama-3.1-405B-Instruct-FP8",
	messages=[
			{"role": "system", "content": "You are a helpful assistant."},
			{"role": "user", "content": "What is deep learning?"},
		],
	stream=True,
	max_tokens=1024,
)

# Iterate and print stream
for message in response:
	print(message.choices[0].delta.content, end="")