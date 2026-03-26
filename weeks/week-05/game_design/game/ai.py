from typing import List, Optional
from game.models import Card, Hand
from game.classifier import HandClassifier, CardType


class AIStrategy:

    TYPE_SCORES = {
        CardType.SINGLE: 1,
        CardType.PAIR: 2,
        CardType.TRIPLE: 3,
        CardType.STRAIGHT: 4,
        CardType.FLUSH: 5,
        CardType.FULL_HOUSE: 6,
        CardType.FOUR_OF_A_KIND: 7,
        CardType.STRAIGHT_FLUSH: 8
    }

    EMPTY_HAND_BONUS = 10000
    NEAR_EMPTY_BONUS = 500
    SPADE_BONUS = 5

    @staticmethod
    def score_play(cards: List[Card], hand: Hand, is_first: bool = False) -> float:
        if not cards:
            return -1

        classification = HandClassifier.classify(cards)
        if classification is None:
            return -1

        type_score = AIStrategy.TYPE_SCORES.get(classification[0], 0)
        rank_score = classification[1]
        suit_score = classification[2]

        score = type_score * 100 + rank_score * 10

        remaining = len(hand) - len(cards)
        if remaining == 0:
            score += AIStrategy.EMPTY_HAND_BONUS
        elif remaining <= 2:
            score += AIStrategy.NEAR_EMPTY_BONUS

        for card in cards:
            if card.suit == 3:
                score += AIStrategy.SPADE_BONUS

        return float(score)

    @staticmethod
    def select_best(valid_plays: List[List[Card]], hand: Hand, is_first: bool = False) -> Optional[List[Card]]:
        if not valid_plays:
            return None

        if is_first:
            for play in valid_plays:
                if len(play) == 1 and play[0].rank == 3 and play[0].suit == 0:
                    return play
            return None

        best_play = None
        best_score = -1

        for play in valid_plays:
            score = AIStrategy.score_play(play, hand, is_first)
            if score > best_score:
                best_score = score
                best_play = play

        return best_play