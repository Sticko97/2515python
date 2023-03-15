import pygame


def main():
    """Main program"""

    # Initialize pygame
    pygame.init()
    # Initialize pygame fonts
    pygame.font.init()

    # Create window
    window = pygame.display.set_mode((500, 500))

    # Create clock instance
    clock = pygame.time.Clock()

    # Create red square
    red_square = pygame.Surface((50, 50)).convert()
    red_square.fill((255, 0, 0))

    # Initial coordinates
    square_x = 250
    square_y = 450

    running = True
    while running:
        # CHANGE THE "FPS" below!
        clock.tick(1)
        # print(pygame.time.get_ticks())
        window.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the keys pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            # Move square right
            square_x = square_x + 10
        elif keys[pygame.K_LEFT]:
            # Move square left
            square_x = square_x - 10

        # Blit the square at its position
        window.blit(red_square, (square_x, square_y))
        pygame.display.update()


if __name__ == "__main__":
    main()
