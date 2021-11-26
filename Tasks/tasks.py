import pygame
import sys
from settings import Settings
from character import Character
from bullet import Bullet


class Tasks:
    """A class for creating the game."""

    def __init__(self):
        """Initialize the class."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Tasks')

        self.character = Character(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Launches the main cycle of the game."""
        while True:
            self._check_events()
            self.character.update()
            self._update_bullets()

            self._update_screen()

    def _check_events(self):
        """Checks events from the keyboard and the mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_events_down(event)
            elif event.type == pygame.KEYUP:
                self._check_events_up(event)

    def _check_events_down(self, event):
        """Checks for pressing buttons."""
        if event.key == pygame.K_UP:
            self.character.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.character.moving_down = True
        # if event.key == pygame.K_RIGHT:
        #     self.character.moving_right = True
        # elif event.key == pygame.K_LEFT:
        #     self.character.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_events_up(self, event):
        """Checks for releasing buttons."""
        # if event.key == pygame.K_RIGHT:
        #     self.character.moving_right = False
        # elif event.key == pygame.K_LEFT:
        #     self.character.moving_left = False
        if event.key == pygame.K_UP:
            self.character.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.character.moving_down = False

    def _update_bullets(self):
        """Updates the bullet position and delete bullets that out of the screen."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.right > self.settings.screen_width:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _fire_bullet(self):
        """Creates new bullet on the screen."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        # Redraws the screen for every cycle.
        self.screen.fill(self.settings.bg_color)
        self.character.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()

        # Displays the last redrawn screen.
        pygame.display.flip()


if __name__ == '__main__':
    # Creates the exemplar and launches the game.
    game = Tasks()
    game.run_game()
