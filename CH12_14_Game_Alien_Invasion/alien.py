import pygame
from pygame.sprite import Sprite
init_direction = 0
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """init alien and set it's position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

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

    def update(self):
        """ move alien to right or left"""
        global init_direction
        if self.ai_settings.fleet_direction != init_direction:
            print("direction:", self.ai_settings.fleet_direction)
            init_direction = self.ai_settings.fleet_direction
            print("init direction:", init_direction)
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """if alien at the screen edge, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


