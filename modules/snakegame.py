import random
import pygame as g
from .snake import Snake
from .berry import SmallBerry, BigBerry
from .audio import AudioPlayer
from .values import *


class SnakeGame:
    def __init__(self):
        self.running = True
        self.paused = False
        g.init()
        self.screen = g.display.set_mode(GAME_SIZE)
        g.display.set_caption("Snake")
        self.clock = g.time.Clock()
        self.snake = self.init_snake()
        self.berry = self.spawn_berry()
        self.direction_x = self.direction_y = 0
        self.last_key = None
        self.game_over = False
        self.score = 1
        self.eating_sound = AudioPlayer(EATING_SOUND_PATH)
        self.end_game_sound = AudioPlayer(END_GAME_SOUND_PATH)

    def init_snake(self):
        x = self.screen.get_width() / 2
        y = self.screen.get_height() / 2
        return Snake(x, y)

    def move_snake(self, x, y, growing):
        self.snake.move(x, y, growing)

    def show_snake(self):
        self.snake.show(self.screen)

    def show_berry(self):
        self.berry.show(self.screen)

    @staticmethod
    def spawn_berry():
        random_value = random.randint(1, 100)
        if random_value % 20 == 0:
            return BigBerry()
        else:
            return SmallBerry()

    def check_game_over(self):
        head = self.snake.get_head()
        x = head['x']
        y = head['y']
        if (x <= 0 or y <= 0 or x >= self.screen.get_width() or
                y >= self.screen.get_height() or self.snake.check_collision_with_body()):
            return True
        return False

    def check_collision(self):
        head = self.snake.get_head()
        snake_x = head['x']
        snake_y = head['y']
        berry_x = self.berry.get_x()
        berry_y = self.berry.get_y()
        if snake_x < berry_x + 27 and snake_x + 13 > berry_x \
                and snake_y < berry_y + 25 and snake_y + 15 > berry_y:
            return True
        return False

    def draw_text(self, message, color, x, y, text_size):
        font = g.font.Font(None, text_size)
        text = font.render(message, True, color)
        text_rect = text.get_rect(center=(x, y))
        self.screen.blit(text, text_rect)

    def handle_keydown(self, event):
        if event.key == g.K_UP and self.last_key != g.K_DOWN:
            self.direction_x, self.direction_y = 0, -5
            self.last_key = g.K_UP
        elif event.key == g.K_LEFT and self.last_key != g.K_RIGHT:
            self.direction_x, self.direction_y = -5, 0
            self.last_key = g.K_LEFT
        elif event.key == g.K_DOWN and self.last_key != g.K_UP:
            self.direction_x, self.direction_y = 0, 5
            self.last_key = g.K_DOWN
        elif event.key == g.K_RIGHT and self.last_key != g.K_LEFT:
            self.direction_x, self.direction_y = 5, 0
            self.last_key = g.K_RIGHT
        elif event.key == g.K_c:
            self.paused = not self.paused

    def handle_pause(self):
        pause_icon = g.image.load(PAUSE_ICON_PATH)
        pause_icon = g.transform.scale(pause_icon, (70, 70))
        self.screen.blit(pause_icon, (self.screen.get_width()/2-35, self.screen.get_height()/2-35))
        g.display.update()
        while self.paused:
            for event in g.event.get():
                if event.type == g.QUIT:
                    self.running = False
                    self.game_over = True
                    self.restart_to_menu()
                if event.type == g.KEYDOWN and event.key == g.K_c:
                    self.paused = not self.paused
                    break

    def handle_events(self):
        for event in g.event.get():
            if event.type == g.QUIT:
                self.running = False
                self.game_over = True
                self.restart_to_menu()
            elif event.type == g.KEYDOWN:
                self.handle_keydown(event)

    def run(self):
        g.time.delay(1000)

        while self.running:
            self.clock.tick(FPS)
            growing = False

            self.handle_events()

            self.screen.fill(PURPLE)
            self.draw_text(f'Your score: {self.score}', ORANGE, 685, 20, 40)

            self.show_berry()
            self.show_snake()
            self.move_snake(self.direction_x, self.direction_y, growing)

            if self.paused:
                self.handle_pause()

            if self.check_game_over():
                self.running = False
                self.end_game_sound.replay()
                self.draw_text(f'Game over, your score: {self.score}', ORANGE,
                               self.screen.get_width() / 2, self.screen.get_height() / 2, 50)
                g.display.update()
                g.time.delay(2200)
                self.restart_to_menu()

            if self.check_collision():
                self.eating_sound.replay()
                if isinstance(self.berry, BigBerry):
                    self.snake.grow(GROW_BIG_BERRY)
                    self.score += GROW_BIG_BERRY
                elif isinstance(self.berry, SmallBerry):
                    self.snake.grow(GROW_SMALL_BERRY)
                    self.score += GROW_SMALL_BERRY
                self.berry = self.spawn_berry()

            g.display.update()

    @staticmethod
    def restart_to_menu():
        from .menu import Menu
        g.quit()
        menu = Menu()
        menu.draw_menu()
