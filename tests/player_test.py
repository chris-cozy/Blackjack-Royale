import unittest
import sys
sys.path.append("..")
from classes.player import Player
from classes.card import Card

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_player_initialization(self):
        self.assertEqual(len(self.player.hand), 0)
        self.assertEqual(self.player.score, 0)

    def test_add_card(self):
        card = Card("8", "Spades")
        self.player.add_card(card)
        self.assertEqual(len(self.player.hand), 1)
        self.assertEqual(self.player.hand[0], card)

    def test_calculate_score(self):
        self.player.add_card(Card("K", "Hearts"))
        self.player.add_card(Card("4", "Clubs"))
        self.assertEqual(self.player.calculate_score(), 14)

if __name__ == '__main__':
    unittest.main()
