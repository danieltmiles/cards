from card import Card
from deck import Deck


class CanastaDeck(Deck):
    def __init__(self):
        Deck.__init__(self)
        for i in xrange(2):
            joker_count = 0
            for suit in Card.Valid_suits:
                for value in Card.Valid_values:
                    if suit == "" and value != "Joker":
                        continue
                    if value == "Joker":
                        if joker_count >= 2:
                            continue
                        joker_count += 1
                    self._cards.append(Card(suit, value))
