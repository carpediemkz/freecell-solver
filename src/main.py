# filepath: freecell-solver/src/main.py

from game.board import Board
from game.solver import Solver
from game.card import Card
from game.card import Suit
from constants import *


def main():
    # Initialize the game board
    # Example suits and ranks for the game
    board = Board()
    board.initialize_board(
        foundation=FOUNDATION, free_cells=FREE_CELLS, suits=SUITS, ranks=RANKS
    )

    # Display the initial state of the board
    board.display_board()

    #######################################################

    # print(board.can_move_column(0, 2, 1))

    #######################################################

    # # Initialize the solver
    # solver = Solver(board)

    # # Start the solving process
    # if solver.find_solution():
    #     print("Solution found!")
    # else:
    #     print("No solution exists.")


if __name__ == "__main__":
    main()
