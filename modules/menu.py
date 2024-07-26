import pygame as g
from .values import *
from .button import Button
from .snakegame import SnakeGame


class Menu:
    def __init__(self):
        g.init()
        self.screen = g.display.set_mode(MENU_SIZE)
        g.display.set_caption("Menu")
        self.clock = g.time.Clock()
        self.running = True
        self.buttons = [
            Button("Start Game", ((self.screen.get_width() / 2), (self.screen.get_height() / 6 - 10)),
                   40, WHITE, TEXT_BUTTON_COLOR, BLACK, 1),
            Button("LeaderBoard", ((self.screen.get_width() / 2), (self.screen.get_height() / 6 + 50)),
                   40, WHITE, TEXT_BUTTON_COLOR, BLACK, 1),
            Button("Sounds", ((self.screen.get_width() / 2), (self.screen.get_height() / 6 + 110)),
                   40, WHITE, TEXT_BUTTON_COLOR, BLACK, 1),
            Button("Exit", ((self.screen.get_width() / 2), (self.screen.get_height() / 6 + 220)),
                   40, WHITE, TEXT_BUTTON_COLOR, BLACK, 1)
        ]

    @staticmethod
    def start_game():
        game = SnakeGame()
        game.run()

    def draw_menu(self):
        while self.running:
            self.clock.tick(FPS)
            self.screen.fill(PURPLE)

            for button in self.buttons:
                button.draw(self.screen)

            self.check_events()
            g.display.update()

    def check_events(self):
        for event in g.event.get():
            if event.type == g.QUIT:
                self.running = False
                break
            for button in self.buttons:
                if button.is_clicked(event):
                    if button.text == "Start Game":
                        self.start_game()
                    elif button.text == "LeaderBoard":
                        self.show_leaderboard()
                    elif button.text == "Exit":
                        self.running = False

    def show_leaderboard(self):
        pass
