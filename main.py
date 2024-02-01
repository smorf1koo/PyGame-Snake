import time

import pygame as g
import random


class Food:
    def __init__(self):
        self.x = random.randint(0, 790)
        self.y = random.randint(0, 590)
        self.color = (0, 0, 255)

    def show(self, screen):
        g.draw.rect(screen, self.color, (self.x, self.y, 10, 10))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.direction_x = self.direction_y = 0
        self.color = (255, 0, 0)
        self.length = 0

    def show(self, screen):
        g.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=1)

    def move(self, direction_1, direction_2):
        self.direction_x = direction_1
        self.direction_y = direction_2
        self.x += self.direction_x
        self.y += self.direction_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


def init_snake(screen):
    x = screen.get_width()/2
    y = screen.get_height()/2
    return Snake(x, y)


def move_snake(snake, x, y):
    snake.move(x, y)


def show_snake(screen, snake):
    snake.show(screen)


def init_food():
    return Food()


def show_food(screen, food):
    food.show(screen)


def check_game_over(screen, snake):
    x = snake.get_x()
    y = snake.get_y()
    if x <= 0 or y <= 0 or x >= screen.get_width() or y >= screen.get_height():
        return True
    else:
        return False


def check_collision(snake, food):
    if snake.get_x() < food.x + 10 and snake.get_x() + snake.width > food.x \
            and snake.get_y() < food.y + 10 and snake.get_y() + snake.height > food.y:
        snake.length += 1
        return True
    else:
        return False


def main():
    size = (800, 600)
    g.init()
    screen = g.display.set_mode(size, g.RESIZABLE)
    # g.display.update()
    g.display.set_caption("Snake")

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    FPS = 30

    game_over = False
    clock = g.time.Clock()
    snake = init_snake(screen)
    food = init_food()
    direction_x = direction_y = 0
    g.time.delay(1000)

    while not game_over:
        clock.tick(FPS)

        for event in g.event.get():
            if event.type == g.QUIT:
                game_over = True
            if event.type == g.KEYDOWN:

                if event.key == g.K_UP:
                    direction_x = 0
                    direction_y = -5
                elif event.key == g.K_LEFT:
                    direction_x = -5
                    direction_y = 0
                elif event.key == g.K_DOWN:
                    direction_x = 0
                    direction_y = 5
                elif event.key == g.K_RIGHT:
                    direction_x = 5
                    direction_y = 0

        screen.fill(BLACK)
        show_food(screen, food)
        show_snake(screen, snake)
        move_snake(snake, direction_x, direction_y)
        if check_game_over(screen, snake):
            game_over = True

        if check_collision(snake, food):
            food = init_food()
        g.display.update()

    time.sleep(2)
    g.quit()
    quit()


if __name__ == '__main__':
    main()
