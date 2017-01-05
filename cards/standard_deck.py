from card import Card
from deck import Deck


class StandardDeck(Deck):
    def __init__(self):
        Deck.__init__(self)
        for suit in Card.Valid_suits:
            for value in Card.Valid_values:
                self._cards.append(Card(suit, value))
