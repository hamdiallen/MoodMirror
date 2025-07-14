import openai
from utils import speak_text

openai.api_key = "YOUR_OPENAI_API_KEY"  # Kendi OpenAI API anahtarını buraya koy

def generate_response_and_speak(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a warm, friendly therapist."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response.choices[0].message.content
        speak_text(reply)
    except Exception:
        speak_text("I'm here for you. Just take a moment to breathe.")
