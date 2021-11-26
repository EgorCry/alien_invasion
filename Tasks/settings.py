class Settings:
    """A class for creating blue sky in 12.1 task."""

    def __init__(self):
        """Initialize the game settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.moving_speed = 1

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
