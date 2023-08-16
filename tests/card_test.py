
import unittest
import sys
sys.path.append("..")
from classes.card import Card



class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card = Card("10", "Hearts")
        self.assertEqual(card.rank, "10")
        self.assertEqual(card.suit, "Hearts")

    def test_card_str_representation(self):
        card = Card("J", "Diamonds")
        self.assertEqual(str(card), "J of Diamonds")

if __name__ == '__main__':
    unittest.main()
