import sys
import pygame


class AlienInvasion:
    """Class for controlling resources and game behavior."""

    def __init__(self):
        """Initializes the game and creates game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Alien Invasion')

        # Creates the screen color.
        self.bg_color = (173, 216, 230)

    def run_game(self):
        """Launches the main cycle of the game."""
        while True:
            # Checks events from the keyboard and the mouse.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraws the screen for every cycle.
            self.screen.fill(self.bg_color)

            # Displays the last redrawn screen.
            pygame.display.flip()


if __name__ == '__main__':
    # Creates the exemplar and launches the game.
    ai = AlienInvasion()
    ai.run_game()
