import random

from abc import ABCMeta


class Deck:
    __metaclass__ = ABCMeta

    def __init__(self):
        raise ValueError("Cannot instantiate abastract class Deck")

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, draw_count=1):
        pass
