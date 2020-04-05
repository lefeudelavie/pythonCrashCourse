import sys
import pygame
from bullet import Bullet

def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # move ship to right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move ship to left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # fire bullets
        fire_bullets(ai_settings, screen, ship, bullets)

def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """reponsed to key down and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def update_bullets(bullets):
    bullets.update()
    # delete disappeard bullets
    for bullet in bullets.copy():
        if bullet.rect.top < 0:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, alien, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    alien.blitme()
    for bullet in bullets:
        bullet.draw_bullet()
    pygame.display.flip()