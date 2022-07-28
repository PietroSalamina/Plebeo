import random

class Card():
    def __init__(self, value, suit) -> None:
        """
        Creates a trump card and assigns it a priority level according to the game rules (*Check README.md)

        Args:
            value (int): face value of the card
            suit (string): suit of the card - "Swords", "Clubs", "Coins" or "Cups"
        """
        self.value = value
        self.suit = suit
        self.priority = self.value - 2
        if self.priority < 1:
            self.priority += 10
        if self.value == 8 and self.suit == "Swords":
            self.priority = 11
    def get_value(self):
        """
        Returns:
            int: face value of the card
        """
        return self.value

    def get_vuit(self):
        """
        Returns:
            string: suit of the card
        """
        return self.suit

    def get_priority(self):
        """
        Returns:
            int: priority value of the card
        """
        return self.priority               
class Deck():
    def __init__(self) -> None:
        """
        Creates a random sequence of 40 trump cards
        """
        suits = ["Swords", "Clubs", "Coins", "Cups"]
        self.cards = []
        self.build(suits)
        self.shuffle()

    def build(self, suits):
        """
        Creates an ordered deck of trump cards

        Args:
            suits (String[]): List of trump card suits
        """
        for suit in suits:
            for i in range(1,11):
                self.cards.append(Card(i, suit))

    def shuffle(self):
        """
        Shuffles a deck of cards
        """
        for i in range (len(self.cards)-1,0,-1):
            r = random.randint(0 , i)
            self.cards[i]  , self.cards[r] = self.cards[r] , self.cards[i]

    def drawCard(self):
        return self.cards.pop()
