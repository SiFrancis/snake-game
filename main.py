import pygame
import math
import config as cfg
import random

class Snake:
    def __init__(self, window: pygame.window.Window) -> None:
        self.window = window
        self.length = 3
        self.body = [
            (1, 1), (2, 1), (3, 1)
        ]
        self.head = self.body[-1]
        self.alive = True
        self.direction = cfg.START_DIR
        self.headcolor = 'green4'
        self.bodycolor = 'green2'

    def update(self, food_list) -> None:

        rows_num = math.ceil(self.window.size[0]/cfg.TILE_SIZE)
        cols_num = math.ceil(self.window.size[1]/cfg.TILE_SIZE)

        if self.alive:
            direc = cfg.DIRECTIONS[self.direction]
            new_head = (
                (self.head[0] + direc[0]) % rows_num, 
                (self.head[1] + direc[1]) % cols_num
            )

            print(new_head)

            if new_head in self.body:
                self.headcolor = 'gray40'
                self.bodycolor = 'gray70'
                self.alive = False
                return

            if new_head in food_list:
                self.length += 1
                food_list.remove(new_head)
                spawnFood(self.window, food_list)

            self.body.append(new_head)

            if len(self.body) > self.length: self.body.pop(0)
            self.head = self.body[-1]

    def draw(self) -> None:
        screen = self.window.get_surface()
        for cell in self.body[:-1]:
            colorCell(cell[0], cell[1], self.bodycolor, screen)

        colorCell(self.head[0], self.head[1], self.headcolor, screen)

def colorCell(x: int, y:int, color:pygame.Color, screen: pygame.Surface):
    colored_rect = pygame.Rect(x*cfg.TILE_SIZE, y*cfg.TILE_SIZE, cfg.TILE_SIZE, cfg.TILE_SIZE)
    pygame.draw.rect(screen, color, colored_rect)

def spawnFood(window: pygame.window.Window, food_list: list[tuple[int, int]]):

    rows_num = math.ceil(window.size[0]/cfg.TILE_SIZE)
    cols_num = math.ceil(window.size[1]/cfg.TILE_SIZE)

    (x, y) = (random.randint(2, rows_num - 2), random.randint(2, cols_num - 2))
    if (x, y) not in food_list:
        food_list.append((x, y))

def main():
    pygame.init()
    window = pygame.Window(size=(cfg.WIDTH, cfg.HEIGHT), title="Simple Snake Game")
    screen = window.get_surface()
    clock = pygame.time.Clock()

    # initialization
    snake = Snake(window)
    food_list = []

    rows_num = math.ceil(window.size[0]/cfg.TILE_SIZE)
    cols_num = math.ceil(window.size[1]/cfg.TILE_SIZE)

    for i in range(cfg.FOOD_AMOUNT):
        spawnFood(window, food_list)

    # main loop
    running = True
    while running:
        # UPDATE PHASE?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if snake.direction != 'left': snake.direction = 'right'
                elif event.key == pygame.K_LEFT:
                    if snake.direction != 'right': snake.direction = 'left'
                elif event.key == pygame.K_UP:
                    if snake.direction != 'down': snake.direction = 'up'
                elif event.key == pygame.K_DOWN:
                    if snake.direction != 'up': snake.direction = 'down'
        
        snake.update(food_list)
        
        # DRAWING PHASE

        # background drawing
        screen.fill('white')

        for food in food_list:
            colorCell(food[0], food[1], "red", screen)

        snake.draw()

        # grid has to be drawn on top of the snake
        for i in range(cols_num):
            for j in range(rows_num):
                tile_rect = pygame.Rect(j*cfg.TILE_SIZE, i*cfg.TILE_SIZE, cfg.TILE_SIZE, cfg.TILE_SIZE)
                pygame.draw.rect(screen, "black", tile_rect, 1, 0)

        window.flip()
        clock.tick(cfg.FPS)
    
    pygame.quit()


if __name__ == "__main__":
    main()
