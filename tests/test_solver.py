import sys
import os
import unittest

# Add the src directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from game.board import Board
from game.solver import Solver, MoveType, Move
from constants import *


class TestSolver(unittest.TestCase):

    def setUp(self):
        board = Board()
        board.initialize_board(
            foundation=FOUNDATION, free_cells=FREE_CELLS, suits=SUITS, ranks=RANKS
        )
        self.solver = Solver()
        self.board = board

    def test_find_solution(self):
        pass

    def test_apply_move(self):
        pass

    def test_is_solved(self):
        pass

    def test_get_possible_moves(self):
        possible_moves = self.solver.get_possible_moves(self.board)
        self.board.display_board()
        self.assertEqual(len(possible_moves), 12)
        free, to_foundation, from_foundation, column = 0, 0, 0, 0
        for move in possible_moves:
            if move.move_type == MoveType.FREE:
                free += 1
            elif move.move_type == MoveType.TO_FOUNDATION:
                to_foundation += 1
            elif move.move_type == MoveType.FROM_FOUNDATION:
                from_foundation += 1
            elif move.move_type == MoveType.COLUMN:
                column += 1
        self.assertEqual(free, 1)
        self.assertEqual(to_foundation, 8)
        self.assertEqual(from_foundation, 0)
        self.assertEqual(column, 3)

        self.board.foundation.append(Card(2, 12))
        possible_moves = self.solver.get_possible_moves(self.board)

        self.board.display_board()
        self.assertEqual(len(possible_moves), 13)
        free, to_foundation, from_foundation, column = 0, 0, 0, 0
        for move in possible_moves:
            if move.move_type == MoveType.FREE:
                free += 1
            elif move.move_type == MoveType.TO_FOUNDATION:
                to_foundation += 1
            elif move.move_type == MoveType.FROM_FOUNDATION:
                from_foundation += 1
            elif move.move_type == MoveType.COLUMN:
                column += 1
        self.assertEqual(free, 1)
        self.assertEqual(to_foundation, 8)
        self.assertEqual(from_foundation, 1)
        self.assertEqual(column, 3)


if __name__ == "__main__":
    unittest.main()
