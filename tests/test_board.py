import sys
import os
import unittest

# Add the src directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from game.board import Board
from game.card import Card
from constants import *


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.initialize_board(
            foundation=FOUNDATION, free_cells=FREE_CELLS, suits=SUITS, ranks=RANKS
        )
        self.should_display_board = False
        self.display_board()

    def display_board(self):
        if self.should_display_board:
            self.board.display_board()

    def test_default_board(self):
        self.assertIsNotNone(self.board)
        self.assertEqual(len(self.board.columns), 8)  # Assuming 8 columns in FreeCell
        self.assertEqual(
            len(self.board.free_cells), 4
        )  # Assuming 4 free cells in FreeCell
        self.assertEqual(
            len(self.board.foundation), 0
        )  # Assuming foundation is empty at the start

    def test_max_cards_to_move(self):
        self.assertEqual(self.board.max_cards_to_move, 5)
        self.board.foundation.append(Card(suit=1, rank=1))
        self.board.update_board_data()
        self.assertEqual(self.board.max_cards_to_move, 4)
        self.board.foundation.append(Card(suit=1, rank=2))
        self.board.update_board_data()
        self.assertEqual(self.board.max_cards_to_move, 3)

        # one empty column
        self.board.columns[0] = []
        self.board.update_board_data()
        self.assertEqual(self.board.max_cards_to_move, 6)

        # two empty columns
        self.board.columns[1] = []
        self.board.update_board_data()
        self.assertEqual(self.board.max_cards_to_move, 12)

    def test_initialize_board(self):
        self.assertIsNotNone(self.board)
        self.assertEqual(len(self.board.columns), 8)  # Assuming 8 columns in FreeCell
        self.assertEqual(
            len(self.board.free_cells), 4
        )  # Assuming 4 free cells in FreeCell
        self.assertEqual(
            len(self.board.foundation), 0
        )  ## Assuming foundation is empty at the start

    def test_free_card(self):
        self.assertFalse(self.board.free_card(Card(suit=1, rank=1)))
        self.assertTrue(self.board.free_card(Card(suit=3, rank=1)))
        self.board.foundation.append(Card(suit=3, rank=2))
        self.display_board()
        self.assertTrue(self.board.free_card(Card(suit=3, rank=2)))
        self.display_board()

    def test_move_cards(self):
        self.assertTrue(self.board.move_cards(0, 2, 1))
        self.assertTrue(self.board.move_cards(7, 3, 1))
        self.assertFalse(self.board.move_cards(7, 3, 2))
        self.assertFalse(self.board.move_cards(2, 3, 1))
        self.assertFalse(self.board.move_cards(4, 5, 1))

        # to the foundation
        self.assertTrue(self.board.move_cards(1, -2, 1))

        # should be handled by free_card
        self.assertFalse(self.board.move_cards(1, -1, 1))

        self.board.columns[2] = [
            Card(suit=2, rank=12),
            Card(suit=4, rank=1),
            Card(suit=3, rank=4),
            Card(suit=3, rank=9),
            Card(suit=1, rank=8),
            Card(suit=3, rank=7),
            Card(suit=1, rank=6),
        ]

        self.assertTrue(self.board.move_cards(4, 2, 1))
        self.assertFalse(self.board.move_cards(2, 4, 5))
        self.assertTrue(self.board.free_card(Card(suit=3, rank=1)))
        self.assertTrue(self.board.move_cards(2, 4, 5))

        self.should_display_board = False
        self.display_board()

    def test_can_foundation(self):
        self.assertTrue(self.board.can_foundation())
        self.board.foundation.append(Card(suit=1, rank=1))
        self.assertTrue(self.board.can_foundation())
        self.board.foundation.append(Card(suit=2, rank=2))
        self.assertTrue(self.board.can_foundation())
        self.board.foundation.append(Card(suit=3, rank=3))
        self.assertTrue(self.board.can_foundation())
        self.board.foundation.append(Card(suit=4, rank=4))
        self.assertFalse(self.board.can_foundation())

    def test_can_free_card(self):
        self.assertFalse(self.board.can_free_card(Card(suit=1, rank=6)))
        self.assertFalse(self.board.can_free_card(Card(suit=2, rank=3)))
        self.assertTrue(self.board.can_free_card(Card(suit=3, rank=1)))
        self.assertFalse(self.board.can_free_card(Card(suit=4, rank=4)))

        self.board.free_cells[0] = Card(suit=1, rank=5)
        self.assertTrue(self.board.can_free_card(Card(suit=1, rank=6)))

    def test_can_move_card(self):

        self.assertFalse(
            self.board.can_move_card(Card(suit=1, rank=1), Card(suit=1, rank=2))
        )
        self.assertTrue(
            self.board.can_move_card(Card(suit=2, rank=3), Card(suit=1, rank=2))
        )
        self.assertTrue(
            self.board.can_move_card(Card(suit=4, rank=4), Card(suit=3, rank=3))
        )
        self.assertFalse(
            self.board.can_move_card(Card(suit=2, rank=4), Card(suit=3, rank=4))
        )

    def test_can_move_column(self):
        # True cases:
        self.assertTrue(self.board.can_move_column(0, 2, 1))
        self.assertTrue(self.board.can_move_column(7, 3, 1))

        # to the foundation
        self.assertTrue(self.board.can_move_column(1, -2, 1))

        self.assertTrue(self.board.can_move_column(1, -1, 1))

        # False cases:
        self.assertFalse(self.board.can_move_column(7, 3, 2))
        self.assertFalse(self.board.can_move_column(2, 3, 1))
        self.assertFalse(self.board.can_move_column(4, 5, 1))

        # self.display_board()
        # self.should_display_board = True

    def test_is_consecutive(self):
        self.assertTrue(self.board.is_consecutive(2, 1))
        self.assertFalse(self.board.is_consecutive(2, 2))

        self.board.columns[2] = [
            Card(suit=2, rank=12),
            Card(suit=4, rank=1),
            Card(suit=3, rank=4),
            Card(suit=2, rank=9),
            Card(suit=1, rank=8),
            Card(suit=2, rank=7),
            Card(suit=1, rank=6),
        ]

        self.assertTrue(self.board.is_consecutive(2, 4))
        self.assertTrue(self.board.is_consecutive(2, 1))
        self.assertTrue(self.board.is_consecutive(2, 2))
        self.assertTrue(self.board.is_consecutive(2, 3))
        self.assertFalse(self.board.is_consecutive(2, 5))


if __name__ == "__main__":
    unittest.main()
