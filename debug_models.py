import google.generativeai as genai

API_KEY = "YOUR_API_KEY_HERE" #Google AI Cloud API

genai.configure(api_key=API_KEY)

print("Searching for available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error connecting: {e}")