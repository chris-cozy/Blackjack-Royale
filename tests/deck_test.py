import unittest
import sys
sys.path.append("..")
from classes.deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_shuffle(self):
        initial_order = self.deck.cards[:]
        self.deck.shuffle()
        shuffled_order = self.deck.cards
        self.assertNotEqual(initial_order, shuffled_order)

    def test_deck_deal(self):
        card = self.deck.deal()
        self.assertIsNotNone(card)
        self.assertEqual(len(self.deck.cards), 51)

if __name__ == '__main__':
    unittest.main()
