import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    # build a ship
    ship = Ship(ai_settings, screen)

    # create bullets
    bullets = Group() 

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

if __name__ == "__main__":
    run_game()