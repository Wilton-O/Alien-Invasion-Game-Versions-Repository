'''
Program:  Alien Invasion Game.
Author:   Wilton Oliver
Purpose:  A school-project remake of the 'Space Invaders' game!
          A player controls a moving, laser-firing ship against enemy aliens. 
          Added score, sound-effects, lives, and game-over conditions.
Date:     11-26-2025 (mm/dd/yyyy)
'''

class GameStats:
    """Specific class for tracking game statistics"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0     # this property should never reset

    def reset_stats(self):
        """Initialize game stats"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

