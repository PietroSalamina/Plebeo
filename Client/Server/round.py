from cards import Deck
from _thread import *
class Round():
    def __init__(self, player_count, max_play_time):
        """
        Initialize the round and create a new deck of cards

        Args:
            player_count (int): number of players
            max_play_time (int): maximum number of seconds before a player skips their turn
        """
        self.player_count = player_count
        self.deck = Deck()
        self.max_play_time = max_play_time
        self.last_played = None
        self.now_playing_ind = 0