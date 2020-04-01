import pygame


class Rocket:
    def __init__(self, er_settings, screen):
        self.er_settings = er_settings
        self.screen = screen

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # put rockt in the middle of the screen
        self.rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.bottom -= self.er_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.er_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.right -= self.er_settings.rocket_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.right += self.er_settings.rocket_speed_factor


