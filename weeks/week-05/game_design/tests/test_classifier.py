import unittest
from game.models import Card
from game.classifier import HandClassifier, CardType


class TestCardType(unittest.TestCase):

    def test_cardtype_values(self):
        self.assertEqual(CardType.SINGLE, 1)
        self.assertEqual(CardType.PAIR, 2)
        self.assertEqual(CardType.TRIPLE, 3)
        self.assertEqual(CardType.STRAIGHT, 4)
        self.assertEqual(CardType.FLUSH, 5)
        self.assertEqual(CardType.FULL_HOUSE, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH, 8)


class TestClassify(unittest.TestCase):

    def test_classify_single_ace(self):
        cards = [Card(14, 3)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.SINGLE)
        self.assertEqual(result[1], 14)
        self.assertEqual(result[2], 3)

    def test_classify_single_two(self):
        cards = [Card(15, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.SINGLE)
        self.assertEqual(result[1], 15)

    def test_classify_single_three(self):
        cards = [Card(3, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.SINGLE)
        self.assertEqual(result[1], 3)

    def test_classify_pair(self):
        cards = [Card(14, 3), Card(14, 2)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.PAIR)
        self.assertEqual(result[1], 14)

    def test_classify_pair_diff_rank(self):
        cards = [Card(14, 3), Card(13, 3)]
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)

    def test_classify_pair_from_three(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]
        result = HandClassifier.classify([cards[0], cards[1]])
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.PAIR)
        self.assertEqual(result[1], 14)

    def test_classify_triple(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.TRIPLE)
        self.assertEqual(result[1], 14)

    def test_classify_triple_not_enough(self):
        cards = [Card(14, 3), Card(13, 2)]
        result = HandClassifier.classify(cards)
        self.assertIsNone(result)

    def test_classify_straight(self):
        cards = [Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.STRAIGHT)
        self.assertEqual(result[1], 7)

    def test_classify_straight_ace_low(self):
        cards = [Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.STRAIGHT)
        self.assertEqual(result[1], 5)

    def test_classify_flush(self):
        cards = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FLUSH)
        self.assertEqual(result[1], 11)

    def test_classify_full_house(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(2, 0), Card(2, 1)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FULL_HOUSE)
        self.assertEqual(result[1], 14)

    def test_classify_four_of_a_kind(self):
        cards = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 1)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.FOUR_OF_A_KIND)
        self.assertEqual(result[1], 14)

    def test_classify_straight_flush(self):
        cards = [Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)]
        result = HandClassifier.classify(cards)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], CardType.STRAIGHT_FLUSH)
        self.assertEqual(result[1], 7)


class TestCompare(unittest.TestCase):

    def test_compare_single_rank(self):
        play1 = [Card(14, 3)]
        play2 = [Card(13, 3)]
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)

    def test_compare_single_suit(self):
        play1 = [Card(14, 3)]
        play2 = [Card(14, 2)]
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)

    def test_compare_pair_rank(self):
        play1 = [Card(14, 3), Card(14, 2)]
        play2 = [Card(13, 3), Card(13, 2)]
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)

    def test_compare_pair_suit(self):
        play1 = [Card(14, 3), Card(14, 2)]
        play2 = [Card(14, 1), Card(14, 0)]
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)

    def test_compare_different_type(self):
        play1 = [Card(14, 3), Card(14, 2)]
        play2 = [Card(15, 0)]
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)

    def test_compare_flush_vs_straight(self):
        play1 = [Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)]
        play2 = [Card(3, 1), Card(4, 2), Card(5, 1), Card(6, 2), Card(7, 1)]
        result = HandClassifier.compare(play1, play2)
        self.assertEqual(result, 1)


class TestCanPlay(unittest.TestCase):

    def test_can_play_first_3clubs(self):
        cards = [Card(3, 0)]
        result = HandClassifier.can_play(None, cards)
        self.assertTrue(result)

    def test_can_play_first_not_3clubs(self):
        cards = [Card(14, 3)]
        result = HandClassifier.can_play(None, cards)
        self.assertFalse(result)

    def test_can_play_same_type(self):
        last_play = [Card(5, 3), Card(5, 2)]
        cards = [Card(6, 3), Card(6, 2)]
        result = HandClassifier.can_play(last_play, cards)
        self.assertTrue(result)

    def test_can_play_diff_type(self):
        last_play = [Card(5, 3), Card(5, 2)]
        cards = [Card(6, 3)]
        result = HandClassifier.can_play(last_play, cards)
        self.assertFalse(result)

    def test_can_play_not_stronger(self):
        last_play = [Card(10, 3), Card(10, 2)]
        cards = [Card(5, 3), Card(5, 2)]
        result = HandClassifier.can_play(last_play, cards)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
