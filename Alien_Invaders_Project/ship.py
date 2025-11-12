'''
Program:  Alien Invasion Game.
Author:   Wilton Oliver
Purpose:  So far, A space game with a ship to control that fires bullets.
Date:     11-12-2025 (mm/dd/yyyy)
'''

import pygame

class Ship:
    """A class managing the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set start position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start new ships at bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store float value for ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Ship movements, starting as not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update ship's position based on the movement."""
        # Update ship's 'x' value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Now update ship's rect value from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
