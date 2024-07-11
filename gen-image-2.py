from openai import OpenAI
client = OpenAI()

response = client.images.edit(
  model="dall-e-2",
  image=open("spider-man.png", "rb"),
  prompt="change the background to chennai ribbon building",
  n=1,
  size="1024x1024"
)
image_url = response.data[0].url

print(image_url)