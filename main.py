from modules.game_logic import *
from modules.berry import *

PURPLE = (88, 2, 109)
ORANGE = (255, 144, 0)
FPS = 30
SIZE = (800, 600)
GROW_BIG_BERRY, GROW_SMALL_BERRY = 5, 1


def main():
    g.init()
    screen = g.display.set_mode(SIZE)
    g.display.set_caption("Snake")

    paused = False
    game_over = False
    last_key = None

    clock = g.time.Clock()
    snake = init_snake(screen)
    berry = spawn_berry()
    direction_x = direction_y = 0
    g.time.delay(1000)
    score = 1

    while not game_over:
        clock.tick(FPS)

        growing = False

        for event in g.event.get():
            if event.type == g.QUIT:
                game_over = True
            if event.type == g.KEYDOWN:
                # Handle key presses to change snake direction
                if event.key == g.K_UP and last_key != g.K_DOWN:
                    direction_x = 0
                    direction_y = -5
                    last_key = g.K_UP
                elif event.key == g.K_LEFT and last_key != g.K_RIGHT:
                    direction_x = -5
                    direction_y = 0
                    last_key = g.K_LEFT
                elif event.key == g.K_DOWN and last_key != g.K_UP:
                    direction_x = 0
                    direction_y = 5
                    last_key = g.K_DOWN
                elif event.key == g.K_RIGHT and last_key != g.K_LEFT:
                    direction_x = 5
                    direction_y = 0
                    last_key = g.K_RIGHT
                elif event.key == g.K_c:
                    paused = not paused

        screen.fill(PURPLE)
        draw_text(screen, f'Your score: {score}', ORANGE,
                  90, 20, 40)

        show_berry(screen, berry)
        show_snake(screen, snake)
        move_snake(snake, direction_x, direction_y, growing)

        while paused:
            for event in g.event.get():
                if event.type == g.KEYDOWN:
                    # Resume the game if 'c' key is pressed
                    if event.key == g.K_c:
                        paused = not paused
                        break

        if check_game_over(screen, snake):
            game_over = True
            draw_text(screen, f'Game over, your score: {score}', ORANGE,
                      screen.get_width()/2, screen.get_height()/2, 50)

        if check_collision(snake, berry):
            berry = spawn_berry()

            if isinstance(berry, BigBerry):
                snake.grow(GROW_BIG_BERRY)
                score += GROW_BIG_BERRY
            elif isinstance(berry, SmallBerry):
                snake.grow(GROW_SMALL_BERRY)
                score += GROW_SMALL_BERRY

        g.display.update()

    g.time.delay(1200)
    g.quit()
    quit()


if __name__ == '__main__':
    main()
