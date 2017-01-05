import copy

from card import Card
from deck import Deck


class StandardDeck(Deck):
    def __init__(self):
        Deck.__init__(self)

        suits = copy.deepcopy(Card.Valid_suits)
        suits.remove("")

        values = copy.deepcopy(Card.Valid_values)
        values.remove("Joker")
        for suit in suits:
            for value in values:
                    self._cards.append(Card(suit, value))
