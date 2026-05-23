import pygame

def main():
    pygame.init()
    window = pygame.Window(size=(640, 480))
    window.title = "Simple Snake Game"
    screen = window.get_surface()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 200))
        window.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()
