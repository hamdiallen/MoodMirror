import random
import os
from utils import speak_text, show_gif, show_image_text

COOLDOWN = {"emotion": None, "frame_count": 0}

def get_random_gif(folder):
    files = [f for f in os.listdir(folder) if f.lower().endswith(".gif")]
    if not files:
        return None
    return os.path.join(folder, random.choice(files))

def handle_emotion(emotion):
    emotion = emotion.lower()
    if emotion == COOLDOWN["emotion"]:
        COOLDOWN["frame_count"] += 1
        if COOLDOWN["frame_count"] < 100:
            return
    COOLDOWN["emotion"] = emotion
    COOLDOWN["frame_count"] = 0

    if emotion == "sad":
        gif_path = get_random_gif("assets")
        if gif_path:
            show_gif(gif_path)
        speak_text("I see you are feeling sad. I'm here for you.")
    elif emotion == "angry":
        show_image_text("Take a deep breath... In... Out...")
        speak_text("Let’s calm down together. Breathe with me.")
    elif emotion == "happy":
        gif_path = get_random_gif("assets")
        if gif_path:
            show_gif(gif_path)
        speak_text("Awesome! You look happy. Keep shining!")
    else:
        # Diğer duygular için de gif göster, konuşma opsiyonel
        gif_path = get_random_gif("assets")
        if gif_path:
            show_gif(gif_path)
