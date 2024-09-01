from openai import OpenAI

client = OpenAI(
	api_key="YOUR_FINE_GRAINED_TOKEN",
	base_url="https://huggingface.co/api/integrations/dgx/v1",
)
response = client.chat.completions.create(
	model="meta-llama/Meta-Llama-3.1-70B-Instruct",
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