# filepath: freecell-solver/src/main.py

from game.board import Board
from game.solver import Solver
from game.card import Card
from game.card import Suit


def main():
    # Initialize the game board
    # Example suits and ranks for the game
    board = Board()
    foundation = []
    free_cells = [Card(suit=i + 1, rank=0) for i in range(4)]
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

    board.initialize_board(
        foundation=foundation, free_cells=free_cells, suits=suits, ranks=ranks
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
