import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("外星人入侵")

    # build a ship
    ship = Ship(screen)

    # set background color
    bg_color = (230, 230, 230)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    run_game()