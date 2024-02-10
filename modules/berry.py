import random
import pygame as g


class Berry:
    def __init__(self):
        # Initialize the berry with a random position and choose a random icon
        self.x = random.randint(30, 770)
        self.y = random.randint(30, 570)
        self.icons = ['./images/berry_icons/berry_icon_1.png',
                      './images/berry_icons/berry_icon_2.png',
                      './images/berry_icons/berry_icon_3.png',
                      './images/berry_icons/berry_icon_4.png']
        self.icon_path = self.icons[random.randint(0, 3)]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class SmallBerry(Berry):
    def show(self, screen):
        # Display a small berry icon on the screen
        icon = g.image.load(self.icon_path)
        icon = g.transform.scale(icon, (30, 30))
        screen.blit(icon, (self.x, self.y))


class BigBerry(Berry):
    def show(self, screen):
        # Display a big berry icon on the screen
        icon = g.image.load(self.icon_path)
        icon = g.transform.scale(icon, (40, 40))
        screen.blit(icon, (self.x, self.y))
