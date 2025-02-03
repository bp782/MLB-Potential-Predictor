# integrate_api.py
import google.generativeai as genai

# Configure the API key
api_key = 'AIzaSyAIB6uyC5AARvIFanwGeziyux0n4NoZLuA'
genai.configure(api_key=api_key)

# Create an instance of the GenerativeModel
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content
response = model.generate_content("Explain how AI works")

# Print the response
print(response.text)
