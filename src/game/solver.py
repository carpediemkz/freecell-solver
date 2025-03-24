from enum import Enum

from game.board import Board
from game.card import Card, Suit


class MoveType(Enum):
    FREE = 1  # Move to a free cell
    FOUNDATION = 2  # Move to the foundation
    COLUMN = 3  # Move to a column


class Move:
    def __init__(
        self, move_type, from_column, to_column, cards_to_move=1, suit_to_free=None
    ):
        self.move_type = move_type
        self.from_column = from_column
        self.to_column = to_column
        self.cards_to_move = cards_to_move
        self.suit_to_free = suit_to_free

    def __str__(self):
        if self.move_type == MoveType.FREE:
            return f"Free {self.suit_to_free}"
        elif self.move_type == MoveType.FOUNDATION:
            return f"foundation column {self.from_column}"
        elif self.move_type == MoveType.COLUMN:
            return f"Move {self.cards_to_move} card(s) from column {self.from_column} to column {self.to_column}"
        else:
            return "Unknown move type"


class Solver:
    def __init__(self, board):
        self.board = board

    def find_solution(self):
        # Implement the logic to find a solution for the FreeCell game
        pass

    def apply_move(self, move):
        # Implement the logic to apply a move to the board
        pass

    def is_solved(self):
        # Implement logic to check if the game is solved
        pass

    def get_possible_moves(self):
        possible_moves = []
        # 1. Check if a card can be moved to a free cell
        for card in self.board.free_cells:
            card_to_free = Card(suit=card.get_index(), rank=card.rank + 1)
            if self.board.can_free_card(card_to_free):
                possible_moves.append(Move(MoveType.FREE, None, None, None, card.suit))

        # 2. Check if a card can be moved to the foundation
        if self.board.can_foundation():
            for i, column in enumerate(self.board.columns):
                if column:
                    possible_moves.append(Move(MoveType.FOUNDATION, i, None))

        # 3. Check if a card can be moved between columns
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
