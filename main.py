import pygame
from settings import Settings
import sys
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    pygame.display.set_caption('Alien Invasion')
    while True:
        screen.fill(ai_settings.background_color)
        ship.bltime()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()
