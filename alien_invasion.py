import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class for controlling resources and game behavior."""

    def __init__(self):
        """Initializes the game and creates game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        """Launches the main cycle of the game."""
        while True:
            self._check_events()
            self.ship.update()

            self._update_screen()

    def _check_events(self):
        """Checks events from the keyboard and the mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Reacts to pressing the buttons."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Reacts to releasing the buttons."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Redraws the screen for every cycle.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Displays the last redrawn screen.
        pygame.display.flip()


if __name__ == '__main__':
    # Creates the exemplar and launches the game.
    ai = AlienInvasion()
    ai.run_game()
