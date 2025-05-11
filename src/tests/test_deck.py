import unittest
from deck import CardDeck


class TestCardDeck(unittest.TestCase):

    def test_deck_initial_size(self):
        deck = CardDeck()
        self.assertEqual(len(deck.deck), 108)

    def test_draw_card_reduces_deck(self):
        deck = CardDeck()
        initial_size = len(deck.deck)
        deck.draw_card()
        self.assertEqual(len(deck.deck), initial_size - 1)

    def test_draw_card_triggers_reshuffle(self):
        deck = CardDeck()
        deck.deck = []
        deck.discard_pile = [
            ("punainen", "5"), ("vihreä", "2"), ("sininen", "7")]
        drawn = deck.draw_card()
        self.assertEqual(len(deck.discard_pile), 1)
        self.assertEqual(len(deck.deck), 1)
        self.assertNotEqual(drawn, ("sininen", "7"))

    def test_no_reshuffle_if_one_card_in_discard(self):
        deck = CardDeck()
        deck.deck = []
        discard = [("punainen", "5")]
        deck.reshuffle_from_discard(discard)
        self.assertEqual(len(discard), 1)
        self.assertEqual(len(deck.deck), 0)

    def test_draw_first_card_skips_wild_card(self):
        deck = CardDeck()
        deck.deck = [("punainen", "5"), ("villi", "")]
        first_card = deck.draw_first_card()
        self.assertEqual(first_card, ("punainen", "5"))
        self.assertIn(("villi", ""), deck.discard_pile)

    def test_draw_card_returns_none_if_no_cards(self):
        deck = CardDeck()
        deck.deck = []
        deck.discard_pile = []
        self.assertIsNone(deck.draw_card())
