class Card(object):
    _valid_suits = ["heart", "spade", "club", "diamond"]
    _red_suits = ["heart", "diamond"]
    _black_suits = ["spade", "club"]
    _valid_values = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    def __init__(self, suit, value):
        if suit not in Card._valid_suits:
            raise ValueError("Unknown suit %s, must be one of %s" % (suit, ", ".join(Card._valid_suits)))
        self.suit = suit
        if value not in Card._valid_values:
            raise ValueError("Unknown card value %s, must be one of %s", (value, ", ".join([str(x) for x in Card._valid_values])))
        self.value = value

        self.color = ""
        if suit in Card._black_suits:
            self.color = "black"
        if suit in Card._red_suits:
            self.color = "red"
