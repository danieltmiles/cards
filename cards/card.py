class Card(object):
    Valid_suits = ["heart", "spade", "club", "diamond", ""]
    Valid_values = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Joker"]
    _red_suits = ["heart", "diamond"]
    _black_suits = ["spade", "club"]

    def __init__(self, suit, value):
        if suit not in Card.Valid_suits:
            raise ValueError("Unknown suit %s, must be one of %s" % (suit, ", ".join(Card.Valid_suits)))
        if (suit == "" or suit is None) and value != "Joker":
            raise ValueError("Everything but the Joker must have a suit")
        self.suit = suit
        if value not in Card.Valid_values:
            raise ValueError("Unknown card value %s, must be one of %s",
                             (value, ", ".join([str(x) for x in Card.Valid_values])))
        self.value = value

        self.color = None
        if suit in Card._black_suits:
            self.color = "black"
        if suit in Card._red_suits:
            self.color = "red"
