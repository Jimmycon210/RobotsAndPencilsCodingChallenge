class Card:
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        """Returns a string representation of the card"""
        return self.value+" of "+self.suit
