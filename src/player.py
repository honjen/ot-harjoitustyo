class Player:
    def __init__(self, deck, num_cards=7):
        self.hand = [deck.draw_card() for _ in range(num_cards)]
        self.last_action = ""

    def play_card(self, index, current_card, is_valid_play):
        if 0 <= index < len(self.hand) and is_valid_play(self.hand[index], current_card):
            return self.hand.pop(index)
        return None

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        self.last_action = ", viimeksi nosti kortin"
