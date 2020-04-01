import pygame
from rocket import Rocket
from settings import Settings
import game_functions as gf

def run_game():
    pygame.init()
    er_settings = Settings()
    screen = pygame.display.set_mode((er_settings.screen_width, er_settings.screen_height))
    pygame.display.set_caption("火箭大作战")

    # build rocket
    rocket = Rocket(er_settings, screen)
    while True:
        gf.check_event(rocket)        
        rocket.update()
        gf.update_screen(er_settings, screen, rocket)


if __name__ == "__main__":
    run_game()
