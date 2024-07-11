from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="king kong running because of the chase from military",
  size="1024x1792",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)