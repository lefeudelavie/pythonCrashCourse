import pygame

class Ship():

    def __init__(self, screen):
        """init ship and set it's place"""
        self.screen = screen

        # load ship image and get it's enclosing rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put every new ship on the bottom, middle place
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """"draw ship in specified place"""
        self.screen.blit(self.image, self.rect)