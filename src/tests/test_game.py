import unittest
from unittest.mock import patch
from game import Game


class FakeRenderer:
    def __init__(self):
        self.message = None

    def draw_end_screen(self, message):
        self.message = message

class TestGame(unittest.TestCase):
    @patch("pygame.time.get_ticks", return_value=1000)
    @patch("pygame.event.get", return_value=[])
    @patch("pygame.quit")
    @patch("sys.exit")
    def setUp(self, *_):
        self.renderer = FakeRenderer()
        self.game = Game(renderer=self.renderer)

    @patch("game.Game._handle_end_screen_input", return_value=None)
    def test_check_game_over_player_wins(self, _):
        self.game.player.hand = []
        self.game.ai.hand = [("vihreä", "3")]
        self.game.check_game_over()
        self.assertIn("Voitit pelin", self.renderer.message)

    @patch("game.Game._handle_end_screen_input", return_value=None)
    def test_check_game_over_ai_wins(self, _):
        self.game.player.hand = [("punainen", "5")]
        self.game.ai.hand = []
        self.game.check_game_over()
        self.assertIn("Hävisit pelin", self.renderer.message)

    @patch("game.Game._handle_end_screen_input", return_value=None)
    def test_check_game_over_draw(self, _):
        self.game.check_game_over(draw=True)
        self.assertIn("tasapeli", self.renderer.message.lower())

    def test_special_card_effects_draw_2(self):
        self.game.ai.hand = [("sininen", "3")]
        self.game._special_card_effects(("punainen", "nosta 2"), is_human=True)
        self.assertEqual(len(self.game.ai.hand), 3)

    @patch("game.Game._choose_random_color", return_value=None)
    def test_special_card_effects_wild_draw_4(self, _):
        self.game.player.hand = [("punainen", "3")]
        self.game._special_card_effects(("villi", "nosta 4"), is_human=False)
        self.assertEqual(len(self.game.player.hand), 5)

    def test_play_card_success(self):
        self.game.current_card = ("punainen", "3")
        self.game.player.hand = [("punainen", "5"), ("sininen", "8")]
        result = self.game._play_card(self.game.player, 0)
        self.assertTrue(result)
        self.assertEqual(self.game.current_card, ("punainen", "5"))
        self.assertEqual(len(self.game.player.hand), 1)

    def test_calculate_score_specials(self):
        hand = [("punainen", "nosta 2"), ("villi", "nosta 4"), ("sininen", "ohita")]
        score = self.game._calculate_score(hand)
        self.assertEqual(score, 20 + 50 + 20)

    def test_ai_turn_draws_card(self):
        self.game.current_card = ("punainen", "5")
        self.game.ai.hand = [("sininen", "3")]
        self.game.turn = "Tietokone"
        self.game._ai_turn()
        self.assertEqual(self.game.turn, "Pelaaja")
        self.assertGreaterEqual(len(self.game.ai.hand), 1)
