import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for bullets control charged by the ship."""

    def __init__(self, ai_game):
        """Creates the object in the current position of the ship."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Creates the bullet in position (0, 0) and the appointment of the right position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Position of the bullet stores in float.
        self.y = float(self.rect.y)

    def update(self):
        """Moves the bullet up on the screen."""
        # Updates the position of the bullet in float.
        self.y -= self.settings.bullet_speed
        # Updates the position of the rectangle.
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Prints the bullet on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
