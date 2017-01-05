import unittest

from cards.canasta_deck import CanastaDeck


class CanastaDeckTest(unittest.TestCase):
    def test_init(self):
        my_deck = CanastaDeck()
        self.assertEquals(len(my_deck._cards), 108)
