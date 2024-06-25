from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="nvidia/nemotron-4-340b-reward",
  messages=[{"role":"user","content":"I am going to Paris, what should I see?"},{"role":"assistant","content":"Ah, Paris, the City of Light! There are so many amazing things to see and do in this beautiful city ..."}],
)
print(completion)
