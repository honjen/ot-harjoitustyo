import unittest
from game import Game


class FakeRenderer:
    def __init__(self):
        self.message = None

    def draw_end_screen(self, message):
        self.message = message


class TestGame(unittest.TestCase):
    def setUp(self):
        self.renderer = FakeRenderer()
        self.game = Game(renderer=self.renderer)

    # is valid same color returns True
    def test_is_valid_play_same_color(self):
        card = ("punainen", "5")
        current = ("punainen", "8")
        self.assertTrue(Game.is_valid_play(card, current))

    # is valid same value returns True
    def test_is_valid_play_same_value(self):
        card = ("vihreä", "5")
        current = ("punainen", "5")
        self.assertTrue(Game.is_valid_play(card, current))

    # is valid different value and color returns False
    def test_is_valid_play_invalid(self):
        card = ("vihreä", "7")
        current = ("punainen", "5")
        self.assertFalse(Game.is_valid_play(card, current))

    # check player win
    def test_check_game_over_player_wins(self):
        self.game.player.hand = []
        self.game.ai.hand = [("vihreä", "5")]
        result = self.game.check_game_over()
        self.assertTrue(result)
        self.assertEqual(self.renderer.message, "Voitit pelin :)")

    # check AI win
    def test_check_game_over_ai_wins(self):
        self.game.player.hand = [("punainen", "1")]
        self.game.ai.hand = []
        result = self.game.check_game_over()
        self.assertTrue(result)
        self.assertEqual(self.renderer.message, "Hävisit pelin :(")

    # check no game over while both have cards
    def test_check_game_over_continues(self):
        self.game.player.hand = [("punainen", "1")]
        self.game.ai.hand = [("vihreä", "2")]
        result = self.game.check_game_over()
        self.assertFalse(result)

    def test_player_special_card_check_nosta2(self):
        card = ("punainen", "nosta 2")
        self.game.player_special_card_check(card)
        self.assertEqual(self.game.ai.last_action, ", viimeksi nosti 2 korttia")

    def test_player_special_card_check_ohita(self):
        card = ("punainen", "ohita")
        self.game.player_special_card_check(card)
        self.assertEqual(self.game.player.last_action, ", sai toisen vuoron")
    
    def test_player_special_card_check_suunnanvaihto(self):
        card = ("punainen", "suunnanvaihto")
        self.game.player_special_card_check(card)
        self.assertEqual(self.game.player.last_action, ", sai toisen vuoron")

    
