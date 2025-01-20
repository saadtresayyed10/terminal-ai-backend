import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")
print(apiKey)