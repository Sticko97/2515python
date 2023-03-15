import pygame


class TextBox(pygame.sprite.Sprite):
    def __init__(self, value=0, size=(50, 50), font_size=24):
        super().__init__()
        self.value = value

        pygame.font.init()
        self.image = pygame.Surface(size)
        self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        self.rect = self.image.get_rect()

    def update(self):
        font_surface = self.font.render(str(self.value), True, (0, 0, 0))
        self.image.fill((255, 255, 255))
        self.image.blit(font_surface, (0, 0))
