import sys
import os
import unittest

# Add the src directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from game.card import Card, Suit

class TestCard(unittest.TestCase):

    def setUp(self):
        self.a_of_hearts = Card(suit=2, rank='A')
        self.seven_of_spades = Card(suit=1, rank=7)
        self.king_of_diamonds = Card(suit=4, rank=13)

    def test_card_properties(self):
        self.assertEqual(self.a_of_hearts.suit, Suit.HEARTS)
        self.assertEqual(self.a_of_hearts.rank, 1)
        print(f"Tested {self.a_of_hearts} properties")

        self.assertEqual(self.seven_of_spades.suit, Suit.SPADES)
        self.assertEqual(self.seven_of_spades.rank, 7)
        print(f"Tested {self.seven_of_spades} properties")

        self.assertEqual(self.king_of_diamonds.suit, Suit.DIAMONDS)
        self.assertEqual(self.king_of_diamonds.rank, 13)
        print(f"Tested {self.king_of_diamonds} properties")

    def test_card_string_representation(self):
        self.assertEqual(str(self.a_of_hearts), '♥️ A')
        print(f"Tested string representation of {self.a_of_hearts}")

        self.assertEqual(str(self.seven_of_spades), '♠️ 7')
        print(f"Tested string representation of {self.seven_of_spades}")

        self.assertEqual(str(self.king_of_diamonds), '♦️ K')
        print(f"Tested string representation of {self.king_of_diamonds}")

    def test_different_color(self):
        self.assertTrue(Card.different_color(Suit.HEARTS, Suit.SPADES))
        self.assertTrue(Card.different_color(Suit.DIAMONDS, Suit.CLUBS))
        self.assertFalse(Card.different_color(Suit.HEARTS, Suit.DIAMONDS))
        self.assertFalse(Card.different_color(Suit.SPADES, Suit.CLUBS))
        print("Tested different_color method")

if __name__ == '__main__':
    unittest.main()