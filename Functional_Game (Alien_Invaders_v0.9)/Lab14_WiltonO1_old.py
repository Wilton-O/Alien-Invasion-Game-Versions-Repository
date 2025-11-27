'''
Program:  Alien Invasion Game.
Author:   Wilton Oliver
Purpose:  A school-project remake of the 'Space Invaders' game!
          A player controls a moving, laser-firing ship against enemy aliens, with lives and end conditions.
Date:     11-26-2025 (mm/dd/yyyy)
'''

# This is the 'main' file. The "alien_invasion.py" file, if you will.
# I named it differently to tell which option of the project-assignment I completed.

import sys, random
from time import sleep     # Using 'sleep' for something other than QoL-reading now :D

import pygame

from button import Button
from game_stats import GameStats
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """General class for game asset management & behavior"""

    def __init__(self):
        """Initialize the game & game resources"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = False

        self.play_button = Button(self, "Press to Play")

    def run_game(self):
        """Start the main game loop"""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()
                
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_play_button(self, mouse_pos):
        """Start new game when play button is pressed"""
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True
    
    def _check_keydown_events(self, event):
        """Respond to keyboard presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to keyboard releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets, Kill old bullets"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
    
    def _ship_hit(self):
        """Respond to ship-alien collisions"""
        if self.stats.ships_left > 0:
            print("Ship Hit!!!")
            self.stats.ships_left -= 1

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        # Kill any colliding bullets and aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Kill remaining bullets, Create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Check if alien in fleet touches a screen edge then update fleet accordingly"""
        self._check_fleet_edges()
        self.aliens.update()

        # Also check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Also check alien-bottom_screen collisions
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Create a fleet of aliens"""
        # Create an alien, place it in a random spot within a row
        # Keep creating aliens until screen is (fairly) filled
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        aliens_per_row = 7
        current_y = alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            # Attempt to place 'aliens_per_row' randomly until rows are satisfied
            for alien in range(aliens_per_row):

                placed = False
                attempts = 0

                while not placed and attempts < 50:
                    attempts += 1

                    random_x = random.randint(
                                            alien_width,
                                            self.settings.screen_width - 2 * alien_width
                                            )
                
                # Attempt placement
                trial = Alien(self)
                trial.rect.x = random_x
                trial.rect.y = current_y

                # Check overlap - erase if overlapping and reattempt
                if not pygame.sprite.spritecollideany(trial, self.aliens):
                    self._create_alien(random_x, current_y)
                    placed = True
        
            # Increment y; After row is finished
            current_y += 2 * alien_height
    
    def _create_alien(self, x_position, y_position):
        """Create alien and place it in a row of the fleet"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond as needed if any aliens reach the screen sides"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _check_aliens_bottom(self):
        """Respond as needed if any aliens reach the screen bottom"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
    
    def _change_fleet_direction(self):
        """If reached screen side, Drop aliens and switch their direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on screen, flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Create game instance, then run the instance
    ai = AlienInvasion()
    ai.run_game()

