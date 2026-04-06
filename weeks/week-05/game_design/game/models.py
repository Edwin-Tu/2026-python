from typing import List, Optional


class Card:
    RANK_SYMBOLS = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}
    SUIT_SYMBOLS = {0: '♣', 1: '♦', 2: '♥', 3: '♠'}

    def __init__(self, rank: int, suit: int):
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.SUIT_SYMBOLS[self.suit]}{self.RANK_SYMBOLS[self.rank]}"

    def __eq__(self, other) -> bool:
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other) -> bool:
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

    def __hash__(self) -> int:
        return hash((self.rank, self.suit))

    def to_sort_key(self):
        return (self.rank, self.suit)


class Deck:
    def __init__(self):
        self.cards = self._create_cards()

    def _create_cards(self) -> List[Card]:
        cards = []
        for rank in range(3, 16):
            for suit in range(4):
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[Card]:
        dealt = self.cards[:n]
        self.cards = self.cards[n:]
        return dealt


class Hand(list):
    def __init__(self, cards: Optional[List[Card]] = None):
        super().__init__(cards or [])

    def sort_desc(self):
        sorted_cards = sorted(self, key=lambda c: (-c.rank, c.suit))
        self.clear()
        self.extend(sorted_cards)

    def find_3_clubs(self) -> Optional[Card]:
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, cards: List[Card]):
        for card in cards:
            for i in range(len(self) - 1, -1, -1):
                if self[i] == card:
                    del self[i]
                    break


class Player:
    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.is_ai = is_ai
        self.hand = Hand()
        self.score = 0

    def take_cards(self, cards: List[Card]):
        self.hand.extend(cards)

    def play_cards(self, cards: List[Card]) -> List[Card]:
        self.hand.remove(cards)
        return cards
