from round import Round
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
        self.round = None
        self.round_count = 0
        start_new_round(self)

def start_new_round(self):  
    """
    Starts a new round and deals each player their hand
    """
    self.round = Round(len(self.players), 60)
    list_of_hands = self.round.deal_hands()

    for i in range(len(self.players)):
        self.players[i].set_hand(list_of_hands[i])
    
def play_cards(self, cards_played):
    return self.round.play_cards(cards_played)

def skip(self):
    return self.round.player_skipped()

    
    