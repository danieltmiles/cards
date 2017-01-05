# Programming exercise as given
> Using Python, please write a set of classes that represent a deck of cards. Classes like "card" and "deck" might be appropriate- but it's entirely up to you. You should be able to "shuffle" the deck. You should also be able to draw cards from the deck one at a time until the deck is empty. Unit tests are required, and the code should be usable from other code. If you want to include a user interface, that's fine, but it's not required.

The solution is broken into two main modules. One for tests, and the other for card operations. They are labeled respectively, "cards," and, "tests."

## Card Class 
The card object represents any given card from the 52 card set of
[French Playing Cards](https://en.wikipedia.org/wiki/French_playing_cards).
That is to say it has four suits with thirteen cards in each suit. The
constructor for a card requires the user to specify the suit and the value
and will validate that the card is valid.

### Methods
 * \__init__(suit, value)
Creates a card with the given suit and value, raising a ValueError if
the combination does not fit within the French Playing Card set.

### Data Members
 * ValidSuits -- list -- A list of the suits available in French Playing Cards
 * ValidValues -- list -- A list of the values available within a suit of French Playing Cards
 * suit -- string -- the suit of the card object
 * value -- string in the case of _ace_, _jack_, _queen_ or _king_, an integer in cases of 2-10
 
## Deck Class -- Abstract, may not be instantiated
### Methods
 * \__init__() to be called by child-class only
 * shuffle() -- None -- SIDE EFFECT, re-order the cards in the deck randomly
 * draw(draw_count=1) -- card object -- SIDE EFFECT, find and return the first _draw_count_ cards in the deck,
 removing them from the list of cards that may be returned in the future. If the deck has no more cards
 to be drawn or if it has fewer than draw_count, it will return None
 
### Data Members
_no public data members_

## StandardDeck Object -- Inherits from Deck
### Methods
 * \__init__() Initializes a deck with the standard 52 cards
 * shuffle() -- None -- Inherited from base class
 * draw(draw_count=1) -- Inherited from base class
 
### Data Members
_no public data members_

## CanastaDeck Object -- Inherits from Deck
### Methods
 * \__init__() Initializes a deck with two sets of the standard 52 cards and four jokers.
 * shuffle() -- None -- Inherited from base class
 * draw(draw_count=1) -- Inherited from base class
 
### Data Members
_no public data members_
