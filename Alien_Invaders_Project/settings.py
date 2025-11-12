'''
Program:  Alien Invasion Game.
Author:   Wilton Oliver
Purpose:  So far, A space game with a ship to control that fires bullets.
Date:     11-12-2025 (mm/dd/yyyy)
'''

class Settings:
    """A class storing all settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 5