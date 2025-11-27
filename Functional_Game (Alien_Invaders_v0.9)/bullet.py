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

class Bullet(Sprite):
    """A class managing bullets fired from ships"""

    def __init__(self, ai_game):
        """Initialize bullet object, start it at ship's current position"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet rect then set correct position
        self.rect = pygame.Rect(
            (0, 0, self.settings.bullet_width, self.settings.bullet_height)
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store float value for bullet's exact position
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet upward on-screen"""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on-screen, play sound"""
        pygame.draw.rect(self.screen, self.color, self.rect)
