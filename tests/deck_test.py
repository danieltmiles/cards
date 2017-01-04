import copy
import unittest

from cards.card import Card
from cards.deck import Deck


class DeckTest(unittest.TestCase):
    def test_init(self):
        my_deck = Deck(Deck.StandardDeck)
        self.assertEquals(len(my_deck.cards), 52)

    # this serves as a reminder to future developers to make unit tests when they implement
    def test_not_implemented(self):
        self.failUnlessRaises(NotImplementedError, Deck, Deck.CanastaDeck)
        self.failUnlessRaises(NotImplementedError, Deck, Deck.PinochleDeck)
        self.failUnlessRaises(NotImplementedError, Deck, Deck.StandardDeckWithJokers)

    def test_shuffle(self):
        my_deck = Deck(Deck.StandardDeck)
        original_order = ", ".join(["%s::%s" % (str(x.value), str(x.suit)) for x in my_deck.cards])

        my_deck.shuffle()
        new_order = ", ".join(["%s::%s" % (str(x.value), str(x.suit)) for x in my_deck.cards])

        self.assertNotEquals(original_order, new_order)

    def test_draw(self):
        my_deck = Deck(Deck.StandardDeck)
        original_cards_length = len(my_deck.cards)
        my_card = my_deck.draw()
        self.assertIsInstance(my_card, Card)
        self.assertEquals(len(my_deck.cards), original_cards_length - 1)
        self.assertEquals(len(my_deck.drawn), 1)

    def test_draw_two(self):
        my_deck = Deck(Deck.StandardDeck)
        original_cards_length = len(my_deck.cards)
        my_cards = my_deck.draw(2)
        self.assertIsInstance(my_cards, list)
        self.assertEquals(len(my_cards), 2)
        self.assertIsInstance(my_cards[0], Card)
        self.assertIsInstance(my_cards[1], Card)
        self.assertEquals(len(my_deck.cards), original_cards_length - 2)
        self.assertEquals(len(my_deck.drawn), 2)

    def test_draw_all(self):
        my_deck = Deck(Deck.StandardDeck)
        original_cards_length = len(my_deck.cards)
        for i in xrange(original_cards_length):
            my_deck.draw()
        my_card = my_deck.draw()

        self.assertIsNone(my_card)
        self.assertEquals(len(my_deck.cards), 0)
        self.assertEquals(len(my_deck.drawn), original_cards_length)

if __name__ == '__main__':
    unittest.main()
