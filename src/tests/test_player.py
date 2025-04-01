import unittest
from deck import CardDeck
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.deck = CardDeck()
        self.player = Player(self.deck)
    
    def test_hand_at_start(self):
        self.assertEqual(len(self.player.hand), 7)
    
    def test_draw_card(self):
        len_player = len(self.player.hand)
        len_deck = len(self.deck.deck)
        self.player.draw_card(self.deck)
        self.assertEqual(len(self.player.hand), len_player + 1)
        self.assertEqual(len(self.deck.deck), len_deck - 1)
    

if __name__ == '__main__':
    unittest.main()
