from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
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

