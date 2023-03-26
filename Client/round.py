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
        self.this_turn_skips = 0
        self.is_new_turn = True
   
    def get_playing_index(self):
        """
        Returns:
            int: index of the now-playing player
        """
        return self.now_playing_ind
    def increase_playing_index(self):
        self.now_playing_ind += 1
        if self.now_playing_ind > self.player_count - 1:
            self.now_playing_ind = 0

    def play_cards(self, cards_played):

        return self       
    