from google import genai

# Replace with your actual Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAQNE0c0POUZRaVfbwWfqUEmkAAV_C9S5s"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Set generation config
generation_config = {
    "temperature": 0.6
}
model = model.with_generation_config(generation_config)

# Example usage
text = "What is the capital of India"
response = model.generate_content(text)
print(response.text) 