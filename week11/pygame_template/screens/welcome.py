import pygame

from components import Button

from .base_screen import BaseScreen


class WelcomeScreen(BaseScreen):
    def __init__(self, window):
        """
        Creates two buttons on the screen.
        """
        super().__init__(window)
        self.sprites = pygame.sprite.Group()

        self.button1 = Button(200, 100, "RED")
        self.button1.rect.x = 100
        self.button1.rect.y = 300

        self.button2 = Button(200, 100, "GREEN")
        self.button2.rect.x = 400
        self.button2.rect.y = 300

        self.sprites.add(self.button1)
        self.sprites.add(self.button2)

    def draw(self):
        """Draws the screen"""
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Clicked on the buttons? Go to the next screen.
            if self.button1.rect.collidepoint(event.pos) or self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "game"

            # Button 1 clicked
            if self.button1.rect.collidepoint(event.pos):
                self.persistent["welcome_button_clicked"] = 1
            # Button 2 clicked
            if self.button2.rect.collidepoint(event.pos):
                self.persistent["welcome_button_clicked"] = 2
