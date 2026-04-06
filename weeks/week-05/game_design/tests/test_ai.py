import unittest
from game.models import Card, Hand
from game.ai import AIStrategy


class TestScorePlay(unittest.TestCase):

    def test_score_single(self):
        hand = Hand([Card(14, 0), Card(3, 0), Card(4, 1), Card(5, 2)])
        cards = [Card(14, 0)]
        score = AIStrategy.score_play(cards, hand)
        self.assertEqual(score, 240)

    def test_score_pair_higher(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        pair_cards = [Card(14, 3), Card(14, 2)]
        single_cards = [Card(3, 0)]
        pair_score = AIStrategy.score_play(pair_cards, hand)
        single_score = AIStrategy.score_play(single_cards, hand)
        self.assertGreater(pair_score, single_score)

    def test_score_triple_higher(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        triple_cards = [Card(14, 3), Card(14, 2), Card(14, 1)]
        pair_cards = [Card(14, 3), Card(14, 2)]
        triple_score = AIStrategy.score_play(triple_cards, hand)
        pair_score = AIStrategy.score_play(pair_cards, hand)
        self.assertGreater(triple_score, pair_score)

    def test_score_near_empty(self):
        hand = Hand([Card(14, 3)])
        cards = [Card(14, 3)]
        score = AIStrategy.score_play(cards, hand)
        self.assertGreater(score, 10000)

    def test_score_low_cards(self):
        hand = Hand([Card(14, 3), Card(3, 0)])
        cards = [Card(14, 3)]
        score = AIStrategy.score_play(cards, hand)
        self.assertGreater(score, 500)

    def test_score_spade_bonus(self):
        hand = Hand([Card(14, 3), Card(3, 0)])
        cards = [Card(14, 3)]
        score = AIStrategy.score_play(cards, hand)
        self.assertEqual(score % 10, 5)


class TestSelectBest(unittest.TestCase):

    def test_select_best(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        valid_plays = [[Card(3, 0)], [Card(14, 3), Card(14, 2)]]
        result = AIStrategy.select_best(valid_plays, hand)
        self.assertEqual(len(result), 2)

    def test_select_first_turn(self):
        hand = Hand([Card(3, 0), Card(14, 3)])
        valid_plays = [[Card(3, 0)], [Card(14, 3)]]
        result = AIStrategy.select_best(valid_plays, hand, is_first=True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].rank, 3)
        self.assertEqual(result[0].suit, 0)

    def test_select_empty(self):
        hand = Hand([Card(3, 0)])
        valid_plays = []
        result = AIStrategy.select_best(valid_plays, hand)
        self.assertIsNone(result)


class TestAIStrategy(unittest.TestCase):

    def test_ai_always_plays(self):
        hand = Hand([Card(14, 3), Card(14, 2)])
        last_play = [Card(3, 0)]
        from game.finder import HandFinder
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play)
        result = AIStrategy.select_best(valid_plays, hand)
        self.assertIsNotNone(result)

    def test_ai_prefers_high(self):
        hand = Hand([Card(14, 3), Card(3, 0)])
        valid_plays = [[Card(3, 0)], [Card(14, 3)]]
        result = AIStrategy.select_best(valid_plays, hand)
        self.assertEqual(result[0].rank, 14)

    def test_ai_try_empty(self):
        hand = Hand([Card(3, 0)])
        valid_plays = [[Card(3, 0)]]
        result = AIStrategy.select_best(valid_plays, hand)
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
