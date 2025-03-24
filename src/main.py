# filepath: freecell-solver/src/main.py

from game.board import Board
from game.solver import Solver, Move, MoveType
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

    # Initialize the solver
    solver = Solver(board)
    possible_moves = solver.get_possible_moves(board)
    for moves in possible_moves:
        print(moves, end="\n")

    print(len(possible_moves))

    move0 = Move(MoveType.FREE, None, None, None, card_to_move=Card(3, 1))
    move1 = Move(MoveType.COLUMN, 0, 2, 1)
    move2 = Move(MoveType.FREE, None, None, None, card_to_move=Card(2, 1))
    move3 = Move(MoveType.COLUMN, 2, 4, 2)

    move1.previous_move = move0
    move2.previous_move = move1
    move3.previous_move = move2
    print(move0.describe())

    board_after_move = solver.apply_move(board_to_move=board, move=move3)
    board_after_move.display_board()

    # # Start the solving process
    # if solver.find_solution():
    #     print("Solution found!")
    # else:
    #     print("No solution exists.")


if __name__ == "__main__":
    main()
