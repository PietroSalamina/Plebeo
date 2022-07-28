
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

def can_play(played_cards):
        for i in range (1, len(played_cards)):
            if played_cards[i].get_value() != played_cards[i-1].get_value():
                return False
        return True

if __name__ == "__main__":
    listOfCards = [Card(1, "Denari"), Card(2,"Spade"), Card(4,"Bastoni"), Card(10, "Coppe"), Card(3, "Denari")]
    card = [Card(1, "Denari"), Card(2, "Spade")]
    test = [Card(1, "Denari"), Card(1, "Coppe"), Card(2, "Spade")]
    print(listOfCards[0].value)
    print(card[0].value)
    if card[0].value == listOfCards[0].value == 2:
        print("Sono un 2")
    else:
        print("Nop")
    bolle = False
    if not bolle:
        print("pipo")
    else:
        print("popi")
    print(can_play(test))