from enum import Enum

from game.board import Board
from game.card import Card, Suit
import copy


class MoveType(Enum):
    FREE = 1  # Move to a free cell
    TO_FOUNDATION = 2  # Move to the foundation
    FROM_FOUNDATION = 3  # Move From the foundation
    COLUMN = 4  # Move to a column


class Move:
    def __init__(
        self,
        move_type,
        from_column,
        to_column,
        cards_to_move: int = 1,
        card_to_move: Card = None,
        previous_move=None,
    ):
        self.move_type = move_type
        self.from_column = from_column
        self.to_column = to_column
        self.cards_to_move = cards_to_move
        self.card_to_move = card_to_move
        self.previous_move = previous_move

    def __str__(self):
        if self.move_type == MoveType.FREE:
            return f"Free {self.card_to_move}"
        elif self.move_type == MoveType.TO_FOUNDATION:
            return f"column to foundation {self.from_column}"
        elif self.move_type == MoveType.FROM_FOUNDATION:
            return f"foundation to column {self.to_column}"
        elif self.move_type == MoveType.COLUMN:
            return f"Move {self.cards_to_move} card(s) from column {self.from_column} to column {self.to_column}"
        else:
            return "Unknown move type"

    def describe(self):
        if self.previous_move:
            return f"{self.previous_move.describe()} -> {self}"
        return str(self)


class Solver:
    def __init__(self, board):
        self.board = board

    def find_solution(self):
        # Implement the logic to find a solution for the FreeCell game
        # Because the stuck game requires a limited number of moves, we can use a bfs algorithm
        queue = self.get_possible_moves(self.board)
        # while queue:
        #     current_board = queue.pop(0)
        #     if current_board.is_solved():
        #         return True

        pass

    def apply_move(self, board_to_move: Board, move: Move) -> Board:
        # Implement the logic to apply a move to the board
        board = copy.deepcopy(board_to_move)
        moves = []
        while move:
            moves.append(move)
            move = move.previous_move
        for move in moves[::-1]:
            if move.move_type == MoveType.FREE:
                board.free_card(move.card_to_move)
            else:
                board.move_cards(move.from_column, move.to_column, move.cards_to_move)
        return board

    def is_solved(self):
        # Implement logic to check if the game is solved
        pass

    def get_possible_moves(self, current_board: Board) -> list:
        possible_moves = []
        # 1. Check if a card can be moved to a free cell
        for column in self.board.columns:
            if column and self.board.can_free_card(column[-1]):
                possible_moves.append(Move(MoveType.FREE, None, None, None, column[-1]))

        # 2. Check if a card can be moved to the foundation
        if self.board.can_foundation():
            for i, column in enumerate(self.board.columns):
                if column:
                    possible_moves.append(Move(MoveType.TO_FOUNDATION, i, None))

        # 3. Check if a card can be moved from the foundation
        if self.board.foundation:
            for card in self.board.foundation:
                for i, column in enumerate(self.board.columns):
                    if column and self.board.can_move_card(column[-1], card):
                        possible_moves.append(
                            Move(MoveType.FROM_FOUNDATION, -2, i, card_to_move=card)
                        )

        # 4. Check if a card can be moved between columns
        for from_column, column in enumerate(self.board.columns):
            if column:
                for to_column, _ in enumerate(self.board.columns):
                    if from_column == to_column:
                        continue
                    for cards_to_move in range(1, self.board.max_cards_to_move + 1):
                        if self.board.can_move_column(
                            from_column, to_column, cards_to_move
                        ):
                            possible_moves.append(
                                Move(
                                    MoveType.COLUMN,
                                    from_column,
                                    to_column,
                                    cards_to_move,
                                )
                            )

        return possible_moves
