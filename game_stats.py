class GameStats:
    """Track stats for the game"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # start alien invasion inactive
        self.game_active = False

        # high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
