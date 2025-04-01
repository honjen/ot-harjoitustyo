import random

class CardDeck:
    def __init__(self):
        colors = ["punainen", "vihreä", "sininen", "keltainen"]
        values = [str(i) for i in range(1, 10)]
        self.deck = [(color, "0") for color in colors] + [(color, value) for color in colors for value in values] * 2
        random.shuffle(self.deck)
    
    def draw_card(self):
        return self.deck.pop() if self.deck else None
