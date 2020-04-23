import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
import game_functions as gf
from button import Button


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")

    # create button "Play"
    play_button = Button(ai_settings, screen, "Play")

    # build a stats instance
    stats = GameStats(ai_settings)
    # build a ship, a bullets group and a aliens group
    ship = Ship(ai_settings, screen)

    # create bullets
    bullets = Group() 

    # create aliens
    aliens = Group()

    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship,
                        aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                         play_button)

if __name__ == "__main__":
    run_game()