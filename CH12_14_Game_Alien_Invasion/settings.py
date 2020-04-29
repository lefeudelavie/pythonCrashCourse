class Settings():
    """Save "Alien invation" setting"""

    def __init__(self):
        """settings for initiate game"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
    
        # ship settings
        self.ship_limit = 3
    

        # bullet setting
        self.bullet_width = 600
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3 

        # alien settings
        self.alien_drop_speed = 10

        # speed up scale for the game
        self.speedup_scale = 3
        # alien point scale speed
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize dynamic settings which will change during game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction 1 is move right, -1 move left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50 # everytime destory an alien, get 50 points


    def increase_speed(self):
        """speed up"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
