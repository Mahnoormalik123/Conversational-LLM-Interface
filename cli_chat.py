import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Roles as system prompts
roles = {
    "Professional Assistant": "You are a professional assistant. Explain things clearly, concisely, and in a formal way.",
    "Creative Companion": "You are a creative and fun companion. Use imagination and friendly tone to explain things.",
    "Technical Expert": "You are a technical expert. Provide detailed, accurate, and technical explanations."
}

question = "Explain Artificial Intelligence in simple words."

# File to save comparison
output_file = "compare_table.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write("=== Prompt Comparison Report ===\n\n")
    f.write(f"Common Question: {question}\n\n")

    for role, prompt in roles.items():
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat(history=[
            {"role": "user", "parts": [prompt]},
        ])
        response = chat.send_message(question)

        f.write(f"--- {role} ---\n")
        f.write(f"Intended Behavior: {prompt}\n")
        f.write(f"Actual Response: {response.text}\n\n")

print(f"Comparison saved in {output_file}")
