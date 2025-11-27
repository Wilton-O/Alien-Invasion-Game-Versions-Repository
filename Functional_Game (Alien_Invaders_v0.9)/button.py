'''
Program:  Alien Invasion Game.
Author:   Wilton Oliver
Purpose:  A school-project remake of the 'Space Invaders' game!
          A player controls a moving, laser-firing ship against enemy aliens. 
          Added score, sound-effects, lives, and game-over conditions.
Date:     11-26-2025 (mm/dd/yyyy)
'''

import pygame.font

class Button:
    """Class to build buttons for the 'Alien Invasion' game"""

    def __init__(self, ai_game, msg):
        """Initialize button properties"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 210, 50           # default_txt-box-size
        self.button_color = (0, 135, 0)             # txt-box
        self.text_color = (255, 255, 255)           # txt-color
        self.font = pygame.font.SysFont(None, 48)   # txt-font/size

        self.rect = pygame.Rect(0, 0, self.width, self.height)  # txt-box-size
        self.rect.center = self.screen_rect.center              # txt-box-alignment

        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into image with txt rendered center on the screen"""
        self.msg_image = self.font.render(msg, True, 
                                          self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw button, then its contained msg"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

