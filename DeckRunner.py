from Deck import Deck
from Card import Card

deck = Deck()
print("Here is our deck:\n",deck.__str__())
print("Shuffling the deck...\n")
deck.shuffle()
print("You are delt one card: ")
print(deck.deal().__str__())