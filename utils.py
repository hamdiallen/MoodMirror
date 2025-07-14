import pyttsx3
import pygame
import cv2
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
import threading
import os
import numpy as np

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def play_music(file):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def show_gif(file):
    app = QApplication.instance()
    if not app:
        app = QApplication([])
    label = QLabel()
    label.setWindowTitle("MoodMirror - GIF")
    label.setAlignment(Qt.AlignCenter)
    movie = QMovie(file)
    label.setMovie(movie)
    movie.start()
    label.resize(500, 500)
    label.show()
    threading.Timer(5, label.close).start()
    app.exec_()

def show_image_text(text):
    img = 255 * np.ones((500, 800, 3), dtype=np.uint8)
    cv2.putText(img, text, (50, 250),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2)
    cv2.imshow("MoodMirror - Visual", img)
    cv2.waitKey(4000)
    cv2.destroyWindow("MoodMirror - Visual")
