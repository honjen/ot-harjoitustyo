import unittest
from deck import CardDeck

class TestCardDeck(unittest.TestCase):
    
    # check deck size at start, wll change to 108 cards when more special cards added
    def test_deck_initial_size(self):
        deck = CardDeck()
        self.assertEqual(len(deck.deck), 100)

    # drawing cards changes deck works
    def test_draw_card_reduces_deck(self):
        deck = CardDeck()
        initial_size = len(deck.deck)
        deck.draw_card()
        self.assertEqual(len(deck.deck), initial_size - 1)

    # drawing card triggers a reshuffle works
    def test_draw_card_triggers_reshuffle(self):
        deck = CardDeck()
        deck.deck = []
        deck.discard_pile = [("punainen", "5"), ("vihreä", "2"), ("sininen", "7")]
        # draw a card -> the deck is empty -> reshuffle automatically
        drawn = deck.draw_card()
        self.assertEqual(len(deck.discard_pile), 1) # 1 card in discard
        self.assertEqual(len(deck.deck), 1)  # 1 card in deck
        self.assertNotEqual(drawn, ("sininen", "7"))  # top discard stays the same
    
    # no reshuffle if only 1 card in discard
    def test_no_reshuffle_if_one_card_in_discard(self):
        deck = CardDeck()
        deck.deck = []
        discard = [("punainen", "5")]
        deck.reshuffle_from_discard(discard)
        self.assertEqual(len(discard), 1) # card stays in discard
        self.assertEqual(len(deck.deck), 0) # empty deck