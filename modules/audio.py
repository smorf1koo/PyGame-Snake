import pygame as g
import threading


class AudioPlayer:
    def __init__(self, file_path):
        self.sound = g.mixer.Sound(file_path)

    def replay(self):
        thread = threading.Thread(target=self.sound.play)
        thread.start()