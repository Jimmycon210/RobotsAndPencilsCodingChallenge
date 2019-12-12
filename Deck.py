import random
from Card import Card
class Deck:

    def __init__(self):
        self.deck = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        for i in suits:
            for j in values:
                self.deck.append(Card(j, i))

    def shuffle(self):
        """Randomly shuffles the deck"""
        random.shuffle(self.deck)


    def deal(self):
        """Removes and returns a card from the deck"""
        if not self.deck: return False # If the deck is empty, return false
        return self.deck.pop(0) 

    def __str__(self):
        """Returns a string representation of the current state of the deck"""
        retStr = "" # Return String
        for card in self.deck:
            retStr += card.__str__()+"\n"
        return retStr


