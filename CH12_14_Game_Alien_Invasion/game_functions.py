import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def get_number_aliens_x(ai_settings, alien_width):
    """Calculate number of aliens in a line"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, alien_height, ship_height):
    """Calculate rows of aliens in screen"""
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create a row of aliens"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_number * alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a fleet of aliens"""
    # create one alien, calcualate how many aliens in a line 
    # the gap between aliens are the width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

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

def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """reponse to key down and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                              bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    """Click Play button to start the game"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # hiden the mouse
        pygame.mouse.set_visible(False)

        # reset game  stat
        stats.reset_stats()
        stats.game_active = True

        # reset score board
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # empty aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a fleet of aliens and put ship in the center
        create_fleet(ai_settings, screen, ship, aliens)

def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(ai_settings, screen, stats, sb, ship, 
                   bullets, aliens):
    """update bullets"""
    bullets.update()
    # delete disappeard bullets
    for bullet in bullets.copy():
        if bullet.rect.top < 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, 
                                  ship, bullets, aliens)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, 
                                  bullets, aliens):
    """ collisions detect and recreate fleet aliens"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    # If collide occur between alien and bullet, scoring
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    # When all the aliens were destroied,  empty the bullets and recreate a fleet of aliens
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()

        # uplevel
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def check_high_score(stats, sb):
    """check if has high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                  play_button):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets:
        bullet.draw_bullet()

    # display the score
    sb.show_score()

    # if game is inactive, draw the Play button
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def check_fleet_edges(ai_settings, aliens):
    """if any alien hit the edge, change the fleet aliens' direction"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """move fleet of aliens down and change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, ship, sb, aliens, bullets, stats):
    """ After aliens hit ship """
    # decrement ship_left
    if stats.ship_left > 0:
        stats.ship_left -= 1

        # update score board
        sb.prep_ships()
    
        # empty bullets and aliens
        bullets.empty()
        aliens.empty()

        # create a new fleet of aliens, and put ship to the middle of the bottom
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """check if has any alien hit the screen edges,and update fleet aliens' position"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check collision between aliens and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, ship, sb, aliens, bullets, stats)

    # check if any alien hit the bottom
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if alien hit the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom > screen_rect.bottom:
            ship_hit(ai_settings, screen, ship, sb, aliens, bullets, stats)
            break
