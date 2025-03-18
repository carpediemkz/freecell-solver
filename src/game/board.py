from game.card import Card
from game.card import Suit


class Board:
    def __init__(self):
        self.foundation = []
        self.free_cells = [Card(suit=i + 1, rank=0) for i in range(4)]
        self.empty_colums = 0
        self.columns = [[] for _ in range(8)]
        self.height = 0
        self.max_cards_to_move = 0
        self.update_board_data()

    def update_board_data(self):
        self.empty_colums = 0
        for column in self.columns:
            self.height = max(self.height, len(column))
            if not column or len(column) == 0:
                self.empty_colums += 1
        empty_foundation = 4 - len(self.foundation)
        self.max_cards_to_move = (1 + empty_foundation) * (2**self.empty_colums)

    def initialize_board(self, suits, ranks):
        # Manually deal the deck to the columns
        for i in range(8):
            size = len(suits[i])
            for index in range(size):
                self.columns[i].append(Card(suit=suits[i][index], rank=ranks[i][index]))
        self.update_board_data()

    def display_board(self):
        print("\nFree Cells Board Start: ", end="\n")
        for i in range(4):
            if i < len(self.foundation):
                print(f"{self.foundation[i]}\t", end="")
            else:
                print(f"{Card(0, 0)}\t", end="")
        for card in self.free_cells:
            print(f"{card}\t", end="")
        print("\n")
        for row in range(self.height):
            for column in range(8):
                if row < len(self.columns[column]):
                    card = self.columns[column][row]
                    print(f"{card}\t", end="")
                else:
                    print("\t", end="")
            print()
        print("\nFree Cells End: ", end="\n")
        print(f"Height: {self.height}")
        print(f"Empty Columns: {self.empty_colums}")

    def move_cards(self, from_column, to_column, cards_to_move):
        if to_column == -2:
            # Move 1 card to the foundation
            if cards_to_move == 1 and self.can_foundation():
                card = self.columns[from_column].pop()
                self.foundation.append(card)
                self.update_board_data()
                return True
            return False
        elif to_column == -1:
            # Move the card to a free cell
            if cards_to_move == 1 and self.can_free(from_column):
                card = self.columns[from_column].pop()
                for i in range(len(self.free_cells)):
                    if (
                        self.free_cells[i].suit == card.suit
                        and self.free_cells[i].rank == card.rank - 1
                    ):  # Find an empty free cell
                        self.free_cells[i] = card
                        self.update_board_data()
                        return True
            return False
        else:
            # Move cards between columns
            if self.can_move_match(from_column, to_column, cards_to_move):
                cards = self.columns[from_column][-cards_to_move:]
                self.columns[from_column] = self.columns[from_column][:-cards_to_move]
                self.columns[to_column].extend(cards)
                self.update_board_data()
                return True
            return False

    def can_foundation(self):
        return len(self.foundation) < 4

    def can_free(self, column):
        if not self.columns[column]:
            return False
        for card in self.free_cells:
            if (
                card.rank == self.columns[column][-1].rank - 1
                and card.suit == self.columns[column][-1].suit
            ):
                return True
        return False

    def can_move_match(self, from_column, to_column, cards_to_move):
        # Implement the logic to check if a card can be moved to the target card
        # This is a placeholder implementation
        if from_column == to_column:
            return False
        if cards_to_move > self.max_cards_to_move:
            return False
        if from_column < 0 or from_column >= len(self.columns):
            return False
        if to_column < 0 or to_column >= len(self.columns):
            return False
        if cards_to_move > len(self.columns[from_column]):
            return False
        if cards_to_move < 1:
            return False
        if self.columns[from_column] == []:
            return False

        card_from = self.columns[from_column][-cards_to_move]
        card_to = self.columns[to_column][-1] if self.columns[to_column] else None
        if card_to:
            # Check if the move is valid based on the game rules
            if (
                not Card.same_color(card_from.suit, card_to.suit)
                and card_from.rank == card_to.rank - 1
            ):
                return True
        elif not card_to:
            # If the target column is empty, any card can be moved
            return True
        return False
