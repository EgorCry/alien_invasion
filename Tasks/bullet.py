import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for bullet."""

    def __init__(self, game):
        """Initialize the sprite."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # Creates the bullet in position (0, 0) and the appointment of the right position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = game.character.rect.midright
        self.rect.y += 5

        # Position of the bullet stores in float.
        self.x = float(self.rect.x)

    def update(self):
        """Moves the bullet up on the screen."""
        # Updates the position of the bullet in float.
        self.x += self.settings.bullet_speed
        # Updates the position of the rectangle.
        self.rect.x = self.x

    def draw_bullet(self):
        """Prints the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
