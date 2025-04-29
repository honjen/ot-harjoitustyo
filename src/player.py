class Player:
    """Represents a player in the card game."""

    def __init__(self, deck, num_cards=7):
        """
        Initializes a player with a hand of cards drawn from the deck.

        Args:
            deck: The card deck object.
            num_cards: The number of cards to draw at the start.
        """
        self.hand = [deck.draw_card() for _ in range(num_cards)]
        self.last_action = ""

    def play_card(self, index, current_card, is_valid_play):
        """
        Plays a card from the player's hand if the play is valid.

        Args:
            index: The index of the card to play in the player's hand.
            current_card: The current card on the discard pile.
            is_valid_play: A function to check if the play is valid.

        Returns:
            The played card if the play is valid, None otherwise.
        """
        if 0 <= index < len(self.hand) and is_valid_play(self.hand[index], current_card):
            return self.hand.pop(index)
        return None

    def draw_card(self, deck):
        """
        Draws a card from the deck and adds it to the player's hand.

        Args:
            deck: The card deck object.

        Returns:
            True if a card was drawn, False otherwise.
        """
        card = deck.draw_card()
        if card:
            self.hand.append(card)
            self.last_action = ", viimeksi nosti kortin"
            return True
        return False
