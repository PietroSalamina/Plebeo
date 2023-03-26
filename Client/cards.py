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