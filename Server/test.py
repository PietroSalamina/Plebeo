from game import Game
from player import Player
if __name__ == "__main__":
    Bituba = Player("Bituba")
    Catta = Player("Catta")
    Savelli = Player("Savelli")
    pipo = Player("pipo")
    ListOfPlay = [Bituba, Catta, Savelli, pipo]
    ThisGame = Game(14, ListOfPlay)
    #print(len(Bituba.hand))
    #print(len(Savelli.hand))
    #print(len(Catta.hand))
    #print(len(pipo.hand))

    print("Bituba" )
    Bituba.showHand()
    print("Savelli" )
    Savelli.showHand()
