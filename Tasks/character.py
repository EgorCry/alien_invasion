import pygame


class Character:
    """A class for character from task 12.2"""

    def __init__(self, task_game):
        """Initialize the ship and set its starting position."""
        self.screen = task_game.screen
        self.screen_rect = task_game.screen.get_rect()
        self.settings = task_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Character presets of position.
        self.y = float(self.rect.y)
        # self.x = float(self.rect.x)

        # Flags for moving.
        # self.moving_right = False
        # self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Updates the position of the character."""
        # if self.moving_right and self.rect.right < self.screen_rect.right:
        #     self.x += self.settings.moving_speed
        # if self.moving_left and self.rect.left > self.screen_rect.left:
        #     self.x -= self.settings.moving_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.moving_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.moving_speed

        # Updates rect by self.x and self.y.
        # self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at the bottom center of the screen."""
        self.screen.blit(pygame.transform.rotate(self.image, -90), self.rect)
