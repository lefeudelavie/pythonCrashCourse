import pygame
import sys

def check_keydown_event(event, rocket):
    if event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True

def check_keyup_event(event, rocket):
    if event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False
    

def check_event(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, rocket) 


def update_screen(er_settings, screen, rocket):
    screen.fill(er_settings.bg_color)
    rocket.blitme()
    pygame.display.flip()      