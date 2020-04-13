class Settings():
    """Save "Alien invation" setting"""

    def __init__(self):
        """settings for initiate game"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3 

        # alien settings
        self.alien_speed_factor = 1
        self.alien_drop_speed = 1
        # fleet_direction 1 is move right, -1 move left
        self.fleet_direction = 1
