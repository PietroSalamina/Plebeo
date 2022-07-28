class Player():
    
    def __init__(self, name):
        self.name = name
        self.game = None
        self.lastRoundPosition = 0
        self.hand = []

    def set_hand(self, dealt_hand):
        self.hand = dealt_hand

    def showHand(self):
        for card in self.hand:
            card.show()

    def can_skip(self):
        return self.game.round.get_is_new_turn()

    def skip(self):
        return self.game.skip()

    def play_card(self, played_cards_ind):
        played_cards = []
        for index in played_cards_ind:
            played_cards.append(self.hand.pop(index))
        if len(self.hand) == 0:
            self.finished_cards()
        return self.game.play_cards(played_cards)

    def finished_cards(self):
        self.lastRoundPosition = self.game.winner_position()


