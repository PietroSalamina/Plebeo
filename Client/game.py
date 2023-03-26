from player import Player
class Game():
    def __init__(self, id, players):
        """
        Initialize the game, once the player treshold is met

        Args:
            id (int): ID Number of the game
            players (Player[]): List of the players in the game
        """
        self.id = id
        self.players = players
