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
        self.solver = Solver(board)

    def test_find_solution(self):
        pass

    def test_apply_move(self):
        pass

    def test_is_solved(self):
        pass

    def test_get_possible_moves(self):
        possible_moves = self.solver.get_possible_moves()
        self.assertEqual(len(possible_moves), 15)
        free, foundation, column = 0, 0, 0
        for move in possible_moves:
            if move.move_type == MoveType.FREE:
                free += 1
            elif move.move_type == MoveType.FOUNDATION:
                foundation += 1
            elif move.move_type == MoveType.COLUMN:
                column += 1
        self.assertEqual(free, 4)
        self.assertEqual(foundation, 8)
        self.assertEqual(column, 3)


if __name__ == "__main__":
    unittest.main()
