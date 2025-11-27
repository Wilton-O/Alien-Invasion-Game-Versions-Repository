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

class Alien(Sprite):
    """A class for a single alien in every fleet."""

    def __init__(self, ai_game):
        """Initialize alien and its start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien bitmap and set its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each alien near top-left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact horizontal position - for movement
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x