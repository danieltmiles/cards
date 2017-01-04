import unittest
from cards.card import Card


class CardTest(unittest.TestCase):
    def test_card_init(self):
        my_card = Card("spade", 2)
        self.assertEquals(my_card.suit, "spade")
        self.assertEquals(my_card.value, 2)
        self.assertEquals(my_card.color, "black")

        my_card = Card("diamond", 2)
        self.assertEquals(my_card.suit, "diamond")
        self.assertEquals(my_card.value, 2)
        self.assertEquals(my_card.color, "red")

    def test_invalid_suit(self):
        self.failUnlessRaises(ValueError, Card, "invalid", 2)

    def test_invalid_value(self):
        self.failUnlessRaises(ValueError, Card, "spade", "invalid")

if __name__ == '__main__':
    unittest.main()
