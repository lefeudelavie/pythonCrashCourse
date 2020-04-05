import pygame
from pygame.sprite import Sprite

class Alien:
    def __init__(self, ai_settings, screen):
        """init alien and set it's position"""
        self.screen = screen
        self.ai_settins = ai_settings

        # load alien's image and set it's rect property
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # init the alien to the screen upperleft
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's accurate position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


