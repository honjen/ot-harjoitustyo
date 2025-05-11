import random


class CardDeck:
    """Represents a deck of cards."""

    def __init__(self):
        """Initializes a deck of cards and shuffles it."""
        colors = ["punainen", "vihreä", "sininen", "keltainen"]
        values = [str(i) for i in range(1, 10)]
        specials = ["ohita", "suunnanvaihto", "nosta 2"]
        self.deck = [(color, "0") for color in colors]
        self.deck += [(color, value)
                      for color in colors for value in values] * 2
        self.deck += [(color, special)
                      for color in colors for special in specials] * 2
        self.deck += [("villi", "")] * 4
        self.deck += [("villi", "nosta 4")] * 4
        random.shuffle(self.deck)
        self.discard_pile = []

    def draw_first_card(self):
        """Draws the first card from the deck, making sure it's not a wild card."""
        while True:
            card = self.draw_card()
            if card[0] != "villi":
                return card
            self.discard_pile.append(card)

    def draw_card(self):
        """Draws a card from the deck. If the deck is empty, reshuffles the discard pile."""
        if not self.deck:
            if len(self.discard_pile) > 1:
                self.reshuffle_from_discard(self.discard_pile)
            if not self.deck:
                return None
        return self.deck.pop()

    def reshuffle_from_discard(self, discard_pile):
        """Reshuffles the discard pile and adds it back to the main deck."""
        if len(discard_pile) > 1:
            top_card = discard_pile.pop()
            random.shuffle(discard_pile)
            self.deck.extend(discard_pile)
            discard_pile.clear()
            discard_pile.append(top_card)
