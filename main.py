import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=apiKey)

print("/t/t/t/tConnected To AI Server/t/t/t/t")

def chatWithBot(prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    if response and hasattr(response, "text"):
        return response.text.strip()
    return "Sorry, failed to understand this..."

if __name__ == "__main__":
    while True:
        userInput = input("You: ")
        if userInput.lower() in ["exit", "end", "quit", "bye", "goodbye"]:
            print("God bless you, bye!")
            break
        response = chatWithBot(userInput)
        print(f"Bot: {response}")