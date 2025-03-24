from game.card import Card, Suit
import copy


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

    def initialize_board(self, foundation, free_cells, suits, ranks):
        self.foundation = copy.deepcopy(foundation)
        self.free_cells = copy.deepcopy(free_cells)
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
                print(f"{'[ ]'}\t", end="")
        for card in self.free_cells:
            if card.rank == 0:
                print(f"{'[ ]'}\t", end="")
            else:
                print(f"{card}\t", end="")
        print("\n")
        for row in range(self.height):
            for column in range(8):
                if row < len(self.columns[column]):
                    card = self.columns[column][row]
                    print(f"{card}\t", end="")
                else:
                    print(f"{Card(2,0)}\t", end="")
            print()
        print("\nFree Cells End: ", end="\n")
        print(f"Height: {self.height}")
        print(f"Empty Columns: {self.empty_colums}")

    def free_card(self, card):
        # find the card in foundation
        for i in range(len(self.foundation)):
            if (
                self.foundation[i].suit == card.suit
                and self.foundation[i].rank == card.rank
            ):
                # remove this card from the foundation
                self.foundation.pop(i)
                self.free_cells[card.get_index() - 1] = card
                self.update_board_data()
                return True
        # find the card in colums:
        for i in range(len(self.columns)):
            if self.columns[i] == []:
                continue
            if (
                self.columns[i][-1].suit == card.suit
                and self.columns[i][-1].rank == card.rank
            ):
                # remove this card from the column
                self.columns[i].pop()
                self.free_cells[card.get_index() - 1] = card
                self.update_board_data()
                return True
        return False

    def move_cards(self, from_column, to_column, cards_to_move):
        # Move 1 card from the foundation to a column
        if from_column == -2:
            if cards_to_move == 1 and self.can_move_card(
                self.foundation[-1], self.columns[to_column][-1]
            ):
                card = self.foundation.pop()
                self.columns[to_column].append(card)
                self.update_board_data()
                return True
            return False
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
            # Handled in free_card()
            return False
        else:
            # Move cards between columns
            if self.can_move_column(from_column, to_column, cards_to_move):
                cards = self.columns[from_column][-cards_to_move:]
                self.columns[from_column] = self.columns[from_column][:-cards_to_move]
                self.columns[to_column].extend(cards)
                self.update_board_data()
                return True
            return False

    def can_foundation(self):
        return len(self.foundation) < 4

    def can_free_card(self, card_to_free):
        return (
            card_to_free.rank == self.free_cells[card_to_free.get_index() - 1].rank + 1
        )

    def can_move_card(self, base_card, moved_card):
        # Implement the logic to check if a card can be moved to the target card
        if not base_card:
            return True
        if Card.different_color(base_card.suit, moved_card.suit):
            return base_card.rank == moved_card.rank + 1
        return False

    def can_move_column(self, from_column, to_column, cards_to_move):
        # Implement the logic to check if a card can be moved to the target card

        # Fast fail checks
        if from_column == to_column:
            return False
        if cards_to_move > self.max_cards_to_move:
            return False
        if to_column not in range(-2, len(self.columns)):
            return False
        if to_column not in range(-2, len(self.columns)):
            return False
        if not (1 <= cards_to_move <= len(self.columns[from_column])):
            return False
        if from_column >= 0 and self.columns[from_column] == []:
            return False

        # Deal with the case of moving to the foundation
        if to_column == -2:
            return self.can_foundation()
        # Deal with the case of moving from the foundation
        if from_column == -2:
            for card in self.foundation:
                if self.can_move_card(card, self.columns[to_column][-1]):
                    return True
            return False

        # Deal with the case of moving to a free cell
        if from_column == -1:
            return False
        if to_column == -1:
            return self.can_free_card(self.columns[from_column][-1])
        # Deal with the case of moving between columns
        card_from = self.columns[from_column][-cards_to_move]
        card_to = self.columns[to_column][-1] if self.columns[to_column] else None
        return self.is_consecutive(from_column, cards_to_move) and self.can_move_card(
            card_to, card_from
        )

    def is_consecutive(self, column, cards_to_move):
        if cards_to_move <= 1:
            return True

        cards = self.columns[column][-cards_to_move:]

        for i in range(-1, -cards_to_move, -1):
            if not self.can_move_card(cards[i - 1], cards[i]):
                return False

        return True
