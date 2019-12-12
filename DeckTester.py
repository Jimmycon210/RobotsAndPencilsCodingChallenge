from Deck import Deck
from Card import Card

sortedDeck = Deck()
shuffledDeck = Deck()
shuffledDeck.shuffle()

firstCard = Card("2", "Diamonds")
aCard = Card("5", "Spades")

assert sortedDeck.__str__ != shuffledDeck.__str__() # sorted and shuffled deck are not in the same order
assert len(shuffledDeck.deck) == 52                 # Deck is still a full 52 card deck
assert type(shuffledDeck.deal()) == type(aCard)     # the deck gives us the top card
assert len(shuffledDeck.deck) == 51                 # One card delt, now it is a 51 card deck

assert sortedDeck.deal().__str__() == firstCard.__str__()  #first card of the unsorted deck is the 2 of Diamonds