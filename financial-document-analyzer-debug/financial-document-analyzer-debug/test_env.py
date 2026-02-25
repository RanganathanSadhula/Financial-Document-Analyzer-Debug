import os
from dotenv import load_dotenv

load_dotenv()

print("Gemini API Key loaded:", os.getenv("GEMINI_API_KEY"))