import pygame
from settings import Settings
import game_functions as gf
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    gf.create_fleet(ai_settings, screen, ship, aliens)
    pygame.display.set_caption('Alien Invasion')
    while True:
        gf.check_events(ship, ai_settings, screen, bullets)
        if stats.game_active:
            ship.updete()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        pygame.display.flip()


run_game()
