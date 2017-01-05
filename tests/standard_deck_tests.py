import copy
import unittest

from cards.card import Card
from cards.standard_deck import StandardDeck


class StandardDeckTest(unittest.TestCase):
    def test_init(self):
        my_deck = StandardDeck()
        self.assertEquals(len(my_deck._cards), 52)

    def test_shuffle(self):
        my_deck = StandardDeck()
        original_order = ", ".join(["%s::%s" % (str(x.value), str(x.suit)) for x in my_deck._cards])

        my_deck.shuffle()
        new_order = ", ".join(["%s::%s" % (str(x.value), str(x.suit)) for x in my_deck._cards])

        self.assertNotEquals(original_order, new_order)

    def test_draw(self):
        my_deck = StandardDeck()
        original_cards_length = len(my_deck._cards)
        my_card = my_deck.draw()
        self.assertIsInstance(my_card, Card)
        self.assertEquals(len(my_deck._cards), original_cards_length - 1)
        self.assertEquals(len(my_deck._drawn), 1)

    def test_draw_two(self):
        my_deck = StandardDeck()
        original_cards_length = len(my_deck._cards)
        my_cards = my_deck.draw(2)
        self.assertIsInstance(my_cards, list)
        self.assertEquals(len(my_cards), 2)
        self.assertIsInstance(my_cards[0], Card)
        self.assertIsInstance(my_cards[1], Card)
        self.assertEquals(len(my_deck._cards), original_cards_length - 2)
        self.assertEquals(len(my_deck._drawn), 2)

    def test_draw_all(self):
        my_deck = StandardDeck()
        original_cards_length = len(my_deck._cards)
        for i in xrange(original_cards_length):
            my_deck.draw()
        my_card = my_deck.draw()

        self.assertIsNone(my_card)
        self.assertEquals(len(my_deck._cards), 0)
        self.assertEquals(len(my_deck._drawn), original_cards_length)

if __name__ == '__main__':
    unittest.main()
