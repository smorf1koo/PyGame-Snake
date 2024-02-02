import time
import pygame as g
import random


class Food:
    def __init__(self):
        self.x = random.randint(0, 790)
        self.y = random.randint(0, 590)
        self.color = (255, 222, 0)

    def show(self, screen):
        g.draw.rect(screen, self.color, (self.x, self.y, 10, 10))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Snake:
    def __init__(self, x, y):
        self.body = [{'x': x, 'y': y}]
        self.width = 10
        self.height = 10
        self.color = (132, 233, 0)
        self.length = 0

    def show(self, screen):
        for section in self.body:
            g.draw.rect(screen, self.color, (section['x'], section['y'], self.width, self.height), border_radius=1)

    def move(self, direction_x, direction_y, growing=False):
        head = {'x': self.body[0]['x'] + direction_x, 'y': self.body[0]['y'] + direction_y}
        self.body.insert(0, head)

        if not growing:
            self.body.pop()

    def check_collision_with_body(self):
        head = self.body[0]
        for section in self.body[1:]:
            if head == section:
                return True
        return False

    def grow(self):
        tail = self.body[-1]
        self.body.append({'x': tail['x'], 'y': tail['y']})

    def get_head(self):
        return self.body[0]


def init_snake(screen):
    x = screen.get_width()/2
    y = screen.get_height()/2
    return Snake(x, y)


def move_snake(snake, x, y, growing):
    snake.move(x, y, growing)


def show_snake(screen, snake):
    snake.show(screen)


def init_food():
    return Food()


def show_food(screen, food):
    food.show(screen)


def check_game_over(screen, snake):
    head = snake.get_head()
    x = head['x']
    y = head['y']
    if x <= 0 or y <= 0 or x >= screen.get_width() or y >= screen.get_height() or snake.check_collision_with_body():
        return True
    return False


def check_collision(snake, food):
    head = snake.get_head()
    snake_x = head['x']
    snake_y = head['y']
    food_x = food.get_x()
    food_y = food.get_y()
    if snake_x < food_x + 10 and snake_x + 10 > food_x \
            and snake_y < food_y + 10 and snake_y + 10 > food_y:
        return True
    return False


def draw_text(screen, message, color, x, y, text_size):
    font = g.font.Font(None, text_size)
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)


def main():
    size = (800, 600)
    g.init()
    screen = g.display.set_mode(size, g.RESIZABLE)
    g.display.set_caption("Snake")

    fps = 30

    game_over = False
    clock = g.time.Clock()
    snake = init_snake(screen)
    food = init_food()
    direction_x = direction_y = 0
    g.time.delay(1000)
    score = 1

    while not game_over:
        clock.tick(fps)

        growing = False
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

        screen.fill((88, 2, 109))  # purple
        show_food(screen, food)
        show_snake(screen, snake)
        move_snake(snake, direction_x, direction_y, growing)

        if check_game_over(screen, snake):
            game_over = True
            draw_text(screen, f'Игра окончена, ваш счет: {score}', (255, 144, 0),
                      screen.get_width()/2, screen.get_height()/2, 50)

        if check_collision(snake, food):
            food = init_food()
            snake.grow()
            # growing = True
            score += 1

        draw_text(screen, f'Ваш счет: {score}', (255, 144, 0),
                  90, 20, 40)
        g.display.update()

    time.sleep(4)
    g.quit()
    quit()


if __name__ == '__main__':
    main()