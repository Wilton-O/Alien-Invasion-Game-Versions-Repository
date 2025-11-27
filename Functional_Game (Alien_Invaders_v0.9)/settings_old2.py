'''
Program:  Alien Invasion Game.
Author:   Wilton Oliver
Purpose:  A school-project remake of the 'Space Invaders' game!
          A player controls a moving, laser-firing ship against enemy aliens, with lives and end conditions.
Date:     11-26-2025 (mm/dd/yyyy)
'''

class Settings:
    """A class storing all settings for Alien Invasion"""

    def __init__(self):
        """Initialize paused game settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 5

        # 'New Round' speed-up settings
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize active game settings"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        self.fleet_direction = 1    # 1 = right; -1 = left
    
    def increase_speed(self):
        """Per-round 'increase speed' settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

