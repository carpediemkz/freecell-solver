import sys
import os
import unittest

# Add the src directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from game.board import Board
from game.card import Card


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # self.board.initialize_board()

    def test_default_board(self):
        self.assertIsNotNone(self.board)
        self.assertEqual(len(self.board.columns), 8)  # Assuming 8 columns in FreeCell
        self.assertEqual(
            len(self.board.free_cells), 4
        )  # Assuming 4 free cells in FreeCell
        self.assertEqual(
            len(self.board.foundation), 4
        )  # Assuming 4 free cells in FreeCell

    def test_max_cards_to_move(self):
        suits = [
            [3, 3, 1, 1, 3, 2, 4],
            [1, 3, 4, 1, 2, 2, 3],
            [3, 3, 1, 1, 2, 4, 3],
            [4, 4, 4, 4, 2, 4, 2],
            [1, 2, 3, 3, 4, 4],
            [1, 3, 2, 3, 2, 1],
            [2, 2, 1, 4, 2, 2],
            [4, 1, 4, 1, 3, 1],
        ]
        ranks = [
            [3, 6, 4, 12, 2, 1, 3],
            [3, 10, 12, 2, 3, 13, 1],
            [7, 9, 8, 6, 12, 1, 4],
            [6, 2, 7, 4, 6, 13, 8],
            [1, 11, 13, 8, 10, 5],
            [5, 5, 7, 11, 5, 13],
            [10, 4, 11, 8, 2, 9],
            [11, 9, 9, 10, 12, 7],
        ]
        self.board.initialize_board(suits, ranks)
        self.assertEqual(self.board.max_cards_to_move, 5)
        self.board.foundation[0] = Card(suit=1, rank=1)
        self.board.update_board_data()
        self.assertEqual(self.board.max_cards_to_move, 4)
        self.board.foundation[1] = Card(suit=1, rank=2)
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

    # def test_initialize_board(self):
    #     self.assertIsNotNone(self.board)
    #     self.assertEqual(len(self.board.columns), 8)  # Assuming 8 columns in FreeCell
    #     self.assertEqual(len(self.board.free_cells), 4)  # Assuming 4 free cells in FreeCell
    #     self.assertEqual(len(self.board.foundation), 4)  # Assuming 4 free cells in FreeCell

    # def test_move_card(self):
    #     initial_position = (0, 0)  # Move from column 0, row 0
    #     target_position = (1, 0)   # Move to column 1, row 0
    #     self.board.move_card(initial_position, target_position)
    #     self.assertIsNone(self.board.columns[0][0])  # Card should be moved from initial position
    #     self.assertIsNotNone(self.board.columns[1][0])  # Card should be present in target position


if __name__ == "__main__":
    unittest.main()
