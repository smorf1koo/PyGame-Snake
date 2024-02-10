import pygame as g
from values import SNAKE_COLOR


class Snake:
    def __init__(self, x, y):
        # Init the snake with a single body segment at the target position
        self.body = [{'x': x, 'y': y}]
        self.width = 15
        self.height = 15
        self.color = SNAKE_COLOR
        self.length = 0
        self.current_direction = (0, 0)

    def show(self, screen):
        # Display the snake on the screen
        for section in self.body:
            g.draw.rect(screen, self.color,
                        (section['x'], section['y'], self.width, self.height),
                        border_radius=1)

    def move(self, direction_x, direction_y, growing=False):
        # Move the snake in the specified direction, and handle growth
        # Check if the new direction is opposite to the current direction
        if ((direction_x, direction_y) !=
                (-self.current_direction[0], -self.current_direction[1])):
            head = {'x': self.body[0]['x'] + direction_x,
                    'y': self.body[0]['y'] + direction_y}
            self.body.insert(0, head)
            self.current_direction = (direction_x, direction_y)

            if not growing:
                self.body.pop()

    def check_collision_with_body(self):
        # Check if the snake collides with itself
        head = self.body[0]
        for section in self.body[1:]:
            if head == section:
                return True
        return False

    def grow(self, n):
        # Increase the length of the snake by 'n'
        for i in range(0, n):
            tail = self.body[-1]
            self.body.append({'x': tail['x'], 'y': tail['y']})

    def get_head(self):
        return self.body[0]
