import random

from abc import ABCMeta


class Deck:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._cards = []
        self._drawn = []

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self, draw_count=1):
        if draw_count < 1 or len(self._cards) < draw_count:
            return None
        cards_to_return = self._cards[0:draw_count]
        self._cards = self._cards[draw_count:]
        self._drawn += cards_to_return
        if draw_count == 1:
            return cards_to_return[0]
        return cards_to_return
