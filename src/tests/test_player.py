import unittest
from deck import CardDeck
from player import Player
from game import Game


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.deck = CardDeck()
        self.player = Player(self.deck)

    #deck has 7 cards at start
    def test_hand_at_start(self):
        self.assertEqual(len(self.player.hand), 7)

    #drawing cards works
    def test_draw_card(self):
        len_player = len(self.player.hand)
        len_deck = len(self.deck.deck)
        self.player.draw_card(self.deck)
        self.assertEqual(len(self.player.hand), len_player + 1)
        self.assertEqual(len(self.deck.deck), len_deck - 1)
   
    #playing a valid card works
    def test_play_card_valid_with_same_color(self):
        self.player.hand = [("punainen", "6")]
        current_card = ("punainen", "5")
        played_card = self.player.play_card(0, current_card, Game.is_valid_play)
        self.assertEqual(played_card, ("punainen", "6"))
        self.assertEqual(len(self.player.hand), 0)

    #playing invalid card does not work
    def test_play_card_invalid_different_color_and_value(self):
        self.player.hand = [("vihreä", "4")]
        current_card = ("punainen", "5")
        played_card = self.player.play_card(0, current_card, Game.is_valid_play)
        self.assertIsNone(played_card)
        self.assertEqual(len(self.player.hand), 1)
