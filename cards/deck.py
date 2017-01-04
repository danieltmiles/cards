import random

from card import Card


class Deck:
    StandardDeck = 1
    CanastaDeck = 2
    PinochleDeck = 3
    StandardDeckWithJokers = 4

    def __init__(self, deck_type):
        try:
            int(deck_type)
        except ValueError:
            deck_type = Deck.StandardDeck
        if deck_type == Deck.StandardDeck:
            self._initialize_standard_deck()
        else:
            raise NotImplementedError

    def _initialize_standard_deck(self):
        self.cards = []
        self.drawn = []
        for suit in Card.Valid_suits:
            for value in Card.Valid_values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, draw_count=1):
        pass
