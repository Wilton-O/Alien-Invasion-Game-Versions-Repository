'''
Program:  Alien Invasion Game.
Author:   Wilton Oliver
Purpose:  A space game with a ship that moves and fires bullets at enemy aliens, with lives and an end condition.
Date:     11-21-2025 (mm/dd/yyyy)
'''

class GameStats:
    """Specific class for tracking game statistics"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize game stats"""
        self.ships_left = self.settings.ship_limit

