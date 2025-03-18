from enum import Enum

class Suit(Enum):
    CLUBS = "Clubs"
    HEARTS = "Hearts"
    SPADES = "Spades"
    DIAMONDS = "Diamonds"

class Card:
    def __init__(self, suit, rank):
        suit_map = {
            1: Suit.SPADES,
            2: Suit.HEARTS,
            3: Suit.CLUBS,
            4: Suit.DIAMONDS
        }
        if suit not in suit_map:
            raise ValueError("Suit must be one of: 1 (Spades), 2 (Hearts), 3 (Clubs), 4 (Diamonds)")
        
        rank_map = {
            "A": 1,
            "J": 11,
            "Q": 12,
            "K": 13
        }
        
        if isinstance(rank, str):
            rank = rank.upper()
            if rank not in rank_map:
                raise ValueError("Rank must be one of: A, J, Q, K or a number between 0 and 13, 0 is only allowed for the free cell zone")
            rank = rank_map[rank]
        elif not (0 <= rank <= 13):
            raise ValueError("Rank must be between 0 and 13")
        
        self.suit = suit_map[suit]
        self.rank = rank

    def __str__(self):
        rank_map = {
            0:  "[]",
            1:  "A",
            11: "J",
            12: "Q",
            13: "K"
        }
        suit_emojis = {
            "Hearts":   "♥️",
            "Clubs":    "♣️",
            "Diamonds": "♦️",
            "Spades":   "♠️"
        }
        rank_str = rank_map.get(self.rank, str(self.rank))
        if self.rank == 0:
            return rank_str
        return f"{suit_emojis.get(self.suit.value, self.suit.value)} {rank_str}"