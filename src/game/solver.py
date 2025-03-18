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
        # Example logic to get possible moves
        for from_column in range(8):
            # Check if the column is not empty
            if not self.board.columns[from_column]:
                continue
            # Check if the card can be moved to a free cell
            if self.board.can_free(from_column):
                possible_moves.append((from_column, -1, 1))
            # Check if the card can be moved to the foundation
            if self.board.can_foundation():
                possible_moves.append((from_column, -2, 1))
            # Check if the card can be moved to any other column
            for to_column in range(8):
                if from_column != to_column:
                    max_cards = min(
                        len(self.board.columns[from_column]),
                        self.board.max_cards_to_move,
                    )
                    if self.board.columns[to_column]:
                        for cards in range(1, max_cards + 1):
                            if self.board.can_move_match(from_column, to_column, cards):
                                possible_moves.append((from_column, to_column, cards))
        return possible_moves
