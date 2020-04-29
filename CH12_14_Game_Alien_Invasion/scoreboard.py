import pygame.font

class Scoreboard():
    """display score class"""

    def __init__(self, ai_settings, screen, stats):
        """initialize properties for display score"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # font used to display score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare for score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """change score to a image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = f'{rounded_score:,}'
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        
        # put the score to the upper right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """change high score to a image"""
        rounded_score = int(round(self.stats.high_score, -1))
        score_str = f'{rounded_score:,}'
        self.high_score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        
        # put the high score to the top center
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20
    
    def prep_level(self):
        """change high score to a image"""
        level = str(self.stats.level)
        self.level_image = self.font.render(level, True, self.text_color,
                                            self.ai_settings.bg_color)
        
        # put the score to the upper right corner
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """display score on screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)