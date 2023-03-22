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
    def deal_hands(self):
        """
        Deals i amounts of hands where i is the player count, 
        and sorts them in the correct other based on the game rules

        Returns:
            List[Card[], ..., Card[]]: list of hands of cards
        """
        list_of_hands = []
        for i in range (self.player_count):
            this_hand = []
            for j in range(40//self.player_count):
                this_hand.append(self.deck.drawCard())
            this_hand.sort(key = lambda x: x.priority)    
            list_of_hands.append(this_hand)
        return list_of_hands

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
        """
        Verifies wether or not a group of cards is valid to be played and if so updates the last group of played cards
        Args:
            cards_played (Card[]): list of cards the player is trying to play

        Returns:
            bool: wether the group of played cards are a valid play
        """
        output = False
        if not self.is_new_turn:
            if len(cards_played) == len(self.last_played):
                if cards_played[0].get_priority() > self.last_played[0].get_priority():
                    self.increase_playing_index()
                    self.last_played = cards_played
                    output = True
            if cards_played[0].get_priority() == 11:
                self.increase_playing_index()
                self.last_played = cards_played
                output = True
                
        else:
            self.increase_playing_index()
            self.last_played = cards_played
            self.is_new_turn = False
            output = True
        return output       
    
    def player_skipped(self):
        """
        Handles the case where a player skips their turn
        """
        self.this_turn_skips += 1
        self.increase_playing_index()
        if self.this_turn_skips == (self.player_count - 1):
            self.this_turn_skips = 0
            self.is_new_turn = True
        return True
            
    def get_is_new_turn(self):
        """
        Check if it is a new turn (if it is you are not allowed to skip)

        Returns:
            bool: wether it's the start of a new turn or not
        """
        return self.is_new_turn