class Card(object):
    Valid_suits = ["heart", "spade", "club", "diamond"]
    Red_suits = ["heart", "diamond"]
    Black_suits = ["spade", "club"]
    Valid_values = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    def __init__(self, suit, value):
        if suit not in Card.Valid_suits:
            raise ValueError("Unknown suit %s, must be one of %s" % (suit, ", ".join(Card.Valid_suits)))
        self.suit = suit
        if value not in Card.Valid_values:
            raise ValueError("Unknown card value %s, must be one of %s", (value, ", ".join([str(x) for x in Card.Valid_values])))
        self.value = value

        self.color = ""
        if suit in Card.Black_suits:
            self.color = "black"
        if suit in Card.Red_suits:
            self.color = "red"
