import pygame


def main():
    """Main program"""

    # Initialize pygame
    pygame.init()

    # Create a window and fill it with a solid color
    window = pygame.display.set_mode((500, 500))
    window.fill((100, 255, 255))

    # Create a Pygame surface, and fill it a solid color
    surf = pygame.Surface((100, 300))
    surf.fill((0, 0, 255))
    # Draw a circle in the surface
    pygame.draw.circle(surf, (255, 0, 0), (50, 50), 100)

    # Display the surface in the window
    window.blit(surf, (0, 50))

    # Update the display
    pygame.display.update()

    # Event loop
    running = True
    while running:
        clock = pygame.time.Clock()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    main()
