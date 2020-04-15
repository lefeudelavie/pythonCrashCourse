class GameStats:
    """Track game statis info"""

    def __init__(self, ai_settings):
        """initiate stat info"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """initiate info which would be updated during game running time"""
        self.ship_left = self.ai_settings.ship_limit
