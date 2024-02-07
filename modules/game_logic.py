import random
import pygame as g
from .snake import Snake
from .berry import SmallBerry, BigBerry


def init_snake(screen):
    # Initialize the snake at the center of the screen
    x = screen.get_width()/2
    y = screen.get_height()/2
    return Snake(x, y)


def move_snake(snake, x, y, growing):
    # Move the snake
    snake.move(x, y, growing)


def show_snake(screen, snake):
    # Display the snake on the screen
    snake.show(screen)


def show_berry(screen, berry):
    # Display the berry on the screen
    berry.show(screen)


def spawn_berry():
    # Randomly choose to spawn a big or small berry
    random_value = random.randint(1, 100)
    if random_value % 20 == 0:
        return BigBerry()
    else:
        return SmallBerry()


def check_game_over(screen, snake):
    # Check if the game is over (snake hits the wall or collides with itself)
    head = snake.get_head()
    x = head['x']
    y = head['y']
    if (x <= 0 or y <= 0 or x >= screen.get_width() or
            y >= screen.get_height() or snake.check_collision_with_body()):
        return True
    return False


def check_collision(snake, berry):
    # Check if the snake collides with the berry
    head = snake.get_head()
    snake_x = head['x']
    snake_y = head['y']
    berry_x = berry.get_x()
    berry_y = berry.get_y()
    if snake_x < berry_x + 27 and snake_x + 13 > berry_x \
            and snake_y < berry_y + 25 and snake_y + 15 > berry_y:
        return True
    return False


def draw_text(screen, message, color, x, y, text_size):
    # Display text on the screen
    font = g.font.Font(None, text_size)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)
