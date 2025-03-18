from game.card import Card
from game.card import Suit


class Board:
    def __init__(self):
        self.columns = [[] for _ in range(8)]
        self.free_cells = [
            Card(suit=i + 1, rank=0) for i in range(4)
        ]  # Free cells initialized with empty cards
        self.height = 0
        self.empty_colums = 0
        self.foundation = [
            Card(suit=i + 1, rank=0) for i in range(4)
        ]
        self.update_board_data()

    def update_board_data(self):
        self.empty_colums = 0
        for column in self.columns:
            self.height = max(self.height, len(column))
            if not column or len(column) == 0:
                self.empty_colums += 1

    def initialize_board(self, suits, ranks):
        # Manually deal the deck to the columns
        for i in range(8):
            size = len(suits[i])
            for index in range(size):
                self.columns[i].append(Card(suit=suits[i][index], rank=ranks[i][index]))
        self.update_board_data()

    def display_board(self):
        print("\nFree Cells Board Start: ", end="\n")
        for card in self.foundation:
            print(f"{card}\t", end="")
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

    def move_card(self, from_column, to_column):
        if self.columns[from_column] and len(self.columns[to_column]) < 13:
            card = self.columns[from_column].pop()
            self.columns[to_column].append(card)
            return True
        return False
