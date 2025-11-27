'''
Program:  Alien Invasion Game.
Author:   Wilton Oliver
Purpose:  A school-project remake of the 'Space Invaders' game!
          A player controls a moving, laser-firing ship against enemy aliens. 
          Added score, sound-effects, lives, and game-over conditions.
Date:     11-26-2025 (mm/dd/yyyy)
'''

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class managing the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship bitmap and set its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start ship at bottom-center of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store ship's exact horizontal position - for movement
        self.x = float(self.rect.x)

        # Ship movements, starting as 'not moving'
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
        
        # Now update ship's rect value from "self.x"
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Place ship at bottom-center"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
