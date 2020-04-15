import pygame
from settings import Settings

class Ship():

    def __init__(self, ai_settings, screen):
        """init ship and set it's place"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image and get it's enclosing rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put every new ship on the bottom, middle place
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)
        # moving flag
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        """"draw ship in specified place"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def update(self):
        """move ship based on moving flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
