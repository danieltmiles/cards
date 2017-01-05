from card import Card
from deck import Deck


class StandardDeck(Deck):
    def __init__(self):
        self.cards = []
        self.drawn = []
        for suit in Card.Valid_suits:
            for value in Card.Valid_values:
                self.cards.append(Card(suit, value))
