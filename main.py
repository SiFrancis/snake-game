import pygame
import math

def colorCell(x: int, y:int, color:pygame.Color, tile_size: int, screen: pygame.Surface):
    colored_rect = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
    pygame.draw.rect(screen, color, colored_rect)

def directionChange():
    pass

def main():
    WIDTH, HEIGHT = 640, 480
    FPS = 5

    pygame.init()
    window = pygame.Window(size=(WIDTH, HEIGHT), title="Simple Snake Game")
    screen = window.get_surface()
    clock = pygame.time.Clock()

    tile_size = 40 # the side length of one grid tile

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # background drawing
        screen.fill('white')

        # PLACEHOLDER - drawing the snake
        colorCell(3, 1, "green4", tile_size, screen)
        colorCell(2, 1, "green2", tile_size, screen)
        colorCell(1, 1, "green2", tile_size, screen)

        # grid has to be drawn on top of the snake
        for i in range(math.ceil(window.size[1]/tile_size)):
            for j in range(math.ceil(window.size[0]/tile_size)):
                tile_rect = pygame.Rect(j*tile_size, i*tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, "black", tile_rect, 1, 0)

        window.flip()
        clock.tick(FPS)
    
    pygame.quit()


if __name__ == "__main__":
    main()
