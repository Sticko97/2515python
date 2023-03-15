import pygame

from components import Shape, TextBox

from .base_screen import BaseScreen


class GameScreen(BaseScreen):
    def __init__(self, window):
        """The game screen has a shape that moves, and a score box"""
        super().__init__(window)

        self.shape = Shape(100, 100, bgcolor=(255, 0, 0), limits=window.get_size())
        self.shape.rect.bottom = window.get_height()
        self.shape.rect.left = window.get_width() / 2 - self.shape.rect.width / 2

        self.scorebox = TextBox()

    def update(self):
        """Deal with key presses outside of the event loop"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.shape.move("left")

        if keys[pygame.K_RIGHT]:
            self.shape.move("right")

        # Make sure we update our scorebox
        self.scorebox.update()
        self.persistent["game_speed"] = self.shape.speed

    def draw(self):
        """Draw the screen"""
        self.window.fill((255, 255, 255))

        # Change the color of the shape depending on the button clicked
        if self.persistent.get("welcome_button_clicked") == 1:
            self.shape.image.fill((255, 0, 0))

        if self.persistent.get("welcome_button_clicked") == 2:
            self.shape.image.fill((0, 255, 0))

        # Draw the sprites
        self.window.blit(self.shape.image, self.shape.rect)
        self.window.blit(self.scorebox.image, self.scorebox.rect)

    def manage_event(self, event):
        """
        Event management for the game screen.
        Pressing space increases the speed of the shape.
        Clicking the mouse stops the game.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Make changes to the attributes of our sprites
                self.scorebox.value += 1
                self.shape.speed += 5

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Stop the game on click
            self.running = False
            self.next_screen = "game_over"
