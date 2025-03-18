import sys
import os
import unittest

# Add the src directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from game.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        # self.board.initialize_board()

    def test_default_board(self):
        self.assertIsNotNone(self.board)
        self.assertEqual(len(self.board.columns), 8)  # Assuming 8 columns in FreeCell
        self.assertEqual(len(self.board.free_cells), 4)  # Assuming 4 free cells in FreeCell
        self.assertEqual(len(self.board.foundation), 4)  # Assuming 4 free cells in FreeCell

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

if __name__ == '__main__':
    unittest.main()