import pygame
import pygame.locals


def create_text_surface(text):
    """This function creates a surface and renders the text argument in it"""

    # Get the default font for the system
    default_font = pygame.font.get_default_font()
    font = pygame.font.Font(default_font, 24)
    text_surface = font.render(text, True, (0, 0, 0))

    return text_surface


def main():
    """Main program"""

    pygame.init()
    # This is required to use pygame's font system
    pygame.font.init()

    window = pygame.display.set_mode((500, 500))

    # Event loop
    running = True
    clock = pygame.time.Clock()
    while running:
        window.fill((255, 255, 255))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False

        pygame.display.update()


if __name__ == "__main__":
    main()
