'''
Program:  Alien Invasion Game.
Author:   Wilton Oliver
Purpose:  A school-project remake of the 'Space Invaders' game!
          A player controls a moving, laser-firing ship against enemy aliens. 
          Added score, sound-effects, lives, and game-over conditions.
Date:     11-26-2025 (mm/dd/yyyy)
'''

import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """Class for the 'Alien Invasion' game score system"""

    def __init__(self, ai_game):
        """Initialize score properties"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_level(self):
        """Render the current game-level as an on-screen image"""
        level_str = str(f"lvl: {self.stats.level}")
        self.level_img = self.font.render(level_str, True,
                                          self.text_color, self.settings.bg_color)
        
        self.level_rect = self.score_img.get_rect()
        self.level_rect.right = self.screen_rect.right - 5       # align level-box 5 px. from right-edge of screen
        self.level_rect.top = self.score_rect.bottom + 10        # align level-box 30 px. from top-edge of screen
    
    def prep_ships(self):
        """Render the current amount of ships left on-screen"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    
    def prep_score(self):
        """Render the score as an on-screen image"""
        rounded_score = round(self.stats.score, -1)
        score_str = (f"pts: {rounded_score:,}")                  # tell the labeled score, using commas as appropriate
        self.score_img = self.font.render(score_str, True,
                                          self.text_color, self.settings.bg_color)
        
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20     # align score-box 20 px. from right-edge of screen
        self.score_rect.top = self.screen_rect.top              # align score-box to top-edge of screen
    
    def prep_high_score(self):
        """Render the hi-score as an on-screen image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = (f"hi: {high_score:,}")                # tell the labeled hi-score, using commas as appropriate
        self.high_score_img = self.font.render(high_score_str, True,
                                               self.text_color, self.settings.bg_color)
        
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx # align hi-score-box center, horizontally
        self.high_score_rect.top = self.screen_rect.top         # align hi-score-box to top-edge of screen
    
    def check_high_score(self):
        """Check for new hi-score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def draw_score(self):
        """Draw score, level, and 'ships left' on-screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.level_img, self.level_rect)
        self.ships.draw(self.screen)

