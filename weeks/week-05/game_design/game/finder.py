from typing import List, Optional
from itertools import combinations
from game.models import Card, Hand
from game.classifier import HandClassifier


class HandFinder:

    @staticmethod
    def find_singles(hand: Hand) -> List[List[Card]]:
        return [[card] for card in hand]

    @staticmethod
    def find_pairs(hand: Hand) -> List[List[Card]]:
        from collections import defaultdict
        rank_groups = defaultdict(list)
        for card in hand:
            rank_groups[card.rank].append(card)

        pairs = []
        for rank, cards in rank_groups.items():
            if len(cards) >= 2:
                for combo in combinations(cards, 2):
                    pairs.append(list(combo))
        return pairs

    @staticmethod
    def find_triples(hand: Hand) -> List[List[Card]]:
        from collections import defaultdict
        rank_groups = defaultdict(list)
        for card in hand:
            rank_groups[card.rank].append(card)

        triples = []
        for rank, cards in rank_groups.items():
            if len(cards) >= 3:
                for combo in combinations(cards, 3):
                    triples.append(list(combo))
        return triples

    @staticmethod
    def find_fives(hand: Hand) -> List[List[Card]]:
        results = []

        from collections import defaultdict
        rank_groups = defaultdict(list)
        for card in hand:
            rank_groups[card.rank].append(card)

        four_of_a_kind_ranks = [r for r, c in rank_groups.items() if len(c) >= 4]
        for rank in four_of_a_kind_ranks:
            cards = rank_groups[rank][:4]
            extra_cards = [c for c in hand if c not in cards]
            for extra in extra_cards:
                results.append(cards + [extra])

        full_house_triple_ranks = [r for r, c in rank_groups.items() if len(c) >= 3]
        full_house_pair_ranks = [r for r, c in rank_groups.items() if len(c) >= 2]

        for rank1 in full_house_triple_ranks:
            for rank2 in full_house_pair_ranks:
                if rank1 != rank2 and len(rank_groups[rank1]) >= 3 and len(rank_groups[rank2]) >= 2:
                    triple = rank_groups[rank1][:3]
                    pair = rank_groups[rank2][:2]
                    results.append(triple + pair)

        for straight in HandFinder._find_all_straights(hand):
            results.append(straight)

        for flush in HandFinder._find_all_flushes(hand):
            results.append(flush)

        return results

    @staticmethod
    def _find_straight_from(hand: Hand, start_rank: int) -> Optional[List[Card]]:
        hand_ranks = [c.rank for c in hand]

        if start_rank == 3:
            needed_ace_low = [14, 15, 3, 4, 5]
            if all(r in hand_ranks for r in needed_ace_low):
                cards = []
                for rank in needed_ace_low:
                    found = [c for c in hand if c.rank == rank][0]
                    cards.append(found)
                return cards

        if start_rank == 11:
            needed = [11, 12, 13, 14, 15]
            if all(r in hand_ranks for r in needed):
                cards = []
                for rank in needed:
                    found = [c for c in hand if c.rank == rank][0]
                    cards.append(found)
                return cards

        needed = list(range(start_rank, start_rank + 5))
        if not all(r in hand_ranks for r in needed):
            return None

        cards = []
        for rank in needed:
            found = [c for c in hand if c.rank == rank][0]
            cards.append(found)

        return cards

    @staticmethod
    def _find_all_straights(hand: Hand) -> List[List[Card]]:
        straights = []
        for start in range(3, 15):
            straight = HandFinder._find_straight_from(hand, start)
            if straight:
                straights.append(straight)
        return straights

    @staticmethod
    def _find_all_flushes(hand: Hand) -> List[List[Card]]:
        from collections import defaultdict
        suit_groups = defaultdict(list)
        for card in hand:
            suit_groups[card.suit].append(card)

        flushes = []
        for suit, cards in suit_groups.items():
            if len(cards) >= 5:
                sorted_cards = sorted(cards, key=lambda c: c.rank, reverse=True)
                for combo in combinations(sorted_cards, 5):
                    flush = list(combo)
                    is_straight = HandClassifier._is_straight([c.rank for c in flush])
                    if is_straight:
                        flushes.append(flush)
                    else:
                        flushes.append(flush)
        return flushes

    @staticmethod
    def get_all_valid_plays(hand: Hand, last_play: Optional[List[Card]]) -> List[List[Card]]:
        if last_play is None:
            three_clubs = [c for c in hand if c.rank == 3 and c.suit == 0]
            if three_clubs:
                return [[three_clubs[0]]]
            return []

        all_plays = []

        all_plays.extend(HandFinder.find_singles(hand))
        all_plays.extend(HandFinder.find_pairs(hand))
        all_plays.extend(HandFinder.find_triples(hand))
        all_plays.extend(HandFinder.find_fives(hand))

        valid_plays = []
        for play in all_plays:
            if HandClassifier.can_play(last_play, play):
                valid_plays.append(play)

        return valid_plays