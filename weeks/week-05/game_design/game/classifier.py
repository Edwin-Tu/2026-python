from typing import List, Optional, Tuple
from enum import IntEnum
from game.models import Card


class CardType(IntEnum):
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:

    @staticmethod
    def _is_straight(ranks: List[int]) -> bool:
        if len(ranks) != 5:
            return False
        unique_ranks = sorted(set(ranks))
        if len(unique_ranks) != 5:
            return False
        if unique_ranks == [3, 4, 5, 6, 7]:
            return True
        if unique_ranks == [3, 4, 5, 14, 15]:
            return True
        for i in range(4):
            if unique_ranks[i + 1] - unique_ranks[i] != 1:
                return False
        return True

    @staticmethod
    def _is_flush(suits: List[int]) -> bool:
        return len(suits) == 5 and len(set(suits)) == 1

    @staticmethod
    def _count_ranks(cards: List[Card]) -> List[Tuple[int, int]]:
        from collections import Counter
        rank_counts = Counter(card.rank for card in cards)
        return sorted(rank_counts.items(), key=lambda x: (-x[1], -x[0]))

    @staticmethod
    def classify(cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        if not cards:
            return None

        n = len(cards)
        ranks = [card.rank for card in cards]
        suits = [card.suit for card in cards]
        max_suit = max(suits)

        if n == 1:
            return (CardType.SINGLE, ranks[0], suits[0])

        if n == 2:
            if ranks[0] == ranks[1]:
                return (CardType.PAIR, ranks[0], max_suit)
            return None

        if n == 3:
            if ranks[0] == ranks[1] == ranks[2]:
                return (CardType.TRIPLE, ranks[0], max_suit)
            return None

        if n == 5:
            is_flush = HandClassifier._is_flush(suits)
            is_straight = HandClassifier._is_straight(ranks)

            if is_flush and is_straight:
                flush_straight_rank = max(ranks)
                if sorted(set(ranks)) == [3, 4, 5, 14, 15]:
                    flush_straight_rank = 5
                return (CardType.STRAIGHT_FLUSH, flush_straight_rank, max_suit)

            rank_counts = HandClassifier._count_ranks(cards)
            if rank_counts[0][1] == 4:
                return (CardType.FOUR_OF_A_KIND, rank_counts[0][0], max_suit)
            if rank_counts[0][1] == 3 and rank_counts[1][1] == 2:
                return (CardType.FULL_HOUSE, rank_counts[0][0], max_suit)
            if is_flush:
                return (CardType.FLUSH, max(ranks), max_suit)
            if is_straight:
                straight_rank = max(ranks)
                if sorted(set(ranks)) == [3, 4, 5, 14, 15]:
                    straight_rank = 5
                return (CardType.STRAIGHT, straight_rank, max_suit)

        return None

    @staticmethod
    def compare(play1: List[Card], play2: List[Card]) -> int:
        type1 = HandClassifier.classify(play1)
        type2 = HandClassifier.classify(play2)

        if type1 is None or type2 is None:
            return 0

        if type1[0] != type2[0]:
            return 1 if type1[0] > type2[0] else -1

        if type1[1] != type2[1]:
            return 1 if type1[1] > type2[1] else -1

        return 1 if type1[2] > type2[2] else -1 if type1[2] < type2[2] else 0

    @staticmethod
    def can_play(last_play: Optional[List[Card]], cards: List[Card]) -> bool:
        if last_play is None:
            return len(cards) == 1 and cards[0].rank == 3 and cards[0].suit == 0

        type1 = HandClassifier.classify(last_play)
        type2 = HandClassifier.classify(cards)

        if type1 is None or type2 is None:
            return False

        if type1[0] != type2[0]:
            return False

        if type1[1] != type2[1]:
            return type2[1] > type1[1]

        return type2[2] > type1[2]
