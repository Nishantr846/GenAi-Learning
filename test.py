from google import genai

client = genai.Client(api_key="AIzaSyAQNE0c0POUZRaVfbwWfqUEmkAAV_C9S5s")

response = client.models.generate_content(
    model = "gemini-2.0-flash-001", contents="What is GenAi?"
)
print(response.text)
