from round import Round
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
        self.round = None
        self.round_count = 0
        self.start_new_round()

def start_new_round(self):  
    """
    Starts a new round and deals each player their hand
    """
    self.round = Round()




    
    