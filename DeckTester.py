from Deck import Deck
from Card import Card

sortedDeck = Deck()
shuffledDeck = Deck()
shuffledDeck.shuffle()

firstCard = Card("2", "Diamonds")
aCard = Card("5", "Spades")

assert sortedDeck.__str__ != shuffledDeck.__str__() # sorted and shuffled deck are not in the same order
assert len(shuffledDeck.deck) == 52
assert type(shuffledDeck.deal()) == type(aCard)     # the deck gives us the top card
assert len(shuffledDeck.deck) == 51

assert sortedDeck.deal().__str__() == firstCard.__str__()