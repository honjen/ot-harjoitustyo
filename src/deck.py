import random


class CardDeck:
    def __init__(self):
        colors = ["punainen", "vihreä", "sininen", "keltainen"]
        values = [str(i) for i in range(1, 10)]
        specials = ["ohita", "suunnanvaihto", "nosta 2"]
        self.deck = [(color, "0") for color in colors]
        self.deck += [(color, value)
                      for color in colors for value in values] * 2
        self.deck += [(color, special)
                      for color in colors for special in specials] * 2
        random.shuffle(self.deck)
        self.discard_pile = []

    def draw_card(self):
        if not self.deck:
            self.reshuffle_from_discard(self.discard_pile)
        return self.deck.pop()

    def reshuffle_from_discard(self, discard_pile):
        if len(discard_pile) > 1:
            top_card = discard_pile[-1]
            other_cards = discard_pile[:-1]
            random.shuffle(other_cards)
            self.deck += other_cards
            discard_pile.clear()
            discard_pile.append(top_card)
