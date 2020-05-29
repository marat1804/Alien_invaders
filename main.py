import pygame
from settings import Settings
import game_functions as gf
from ship import Ship
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen, ai_settings)
    bullets = Group()
    pygame.display.set_caption('Alien Invasion')
    while True:
        gf.check_events(ship, ai_settings, screen, bullets)
        ship.updete()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        pygame.display.flip()


run_game()
