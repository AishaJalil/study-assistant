import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()

print("📋 Available Gemini Models:\n")
for m in models:
    try:
        model = genai.GenerativeModel(model_name=m.name)
        # Try a dummy prompt to see if it supports generate_content
        model.generate_content("Hello")
        print(f"✅ {m.name} supports generate_content")
    except Exception as e:
        print(f"❌ {m.name} does NOT support generate_content → {e}")
