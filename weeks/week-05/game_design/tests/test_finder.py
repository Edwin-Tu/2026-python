import unittest
from game.models import Card, Hand
from game.finder import HandFinder
from game.classifier import HandClassifier


class TestFindSingles(unittest.TestCase):

    def test_find_singles(self):
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        result = HandFinder.find_singles(hand)
        self.assertEqual(len(result), 3)

    def test_find_singles_empty(self):
        hand = Hand([])
        result = HandFinder.find_singles(hand)
        self.assertEqual(len(result), 0)


class TestFindPairs(unittest.TestCase):

    def test_find_pairs_one(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        result = HandFinder.find_pairs(hand)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0].rank, 14)

    def test_find_pairs_two(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 0)])
        result = HandFinder.find_pairs(hand)
        self.assertEqual(len(result), 2)

    def test_find_pairs_none(self):
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        result = HandFinder.find_pairs(hand)
        self.assertEqual(len(result), 0)


class TestFindTriples(unittest.TestCase):

    def test_find_triples_one(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        result = HandFinder.find_triples(hand)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0].rank, 14)

    def test_find_triples_with_extra(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 2)])
        result = HandFinder.find_triples(hand)
        self.assertEqual(len(result), 1)


class TestFindFives(unittest.TestCase):

    def test_find_straight(self):
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0), Card(14, 3)])
        result = HandFinder.find_fives(hand)
        types = [HandClassifier.classify(cards) for cards in result]
        straight_types = [t for t in types if t and t[0].value >= 4]
        self.assertGreater(len(straight_types), 0)

    def test_find_flush(self):
        hand = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0), Card(14, 3)])
        result = HandFinder.find_fives(hand)
        types = [HandClassifier.classify(cards) for cards in result]
        flush_types = [t for t in types if t and t[0] == 5]
        self.assertGreater(len(flush_types), 0)

    def test_find_full_house(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 2)])
        result = HandFinder.find_fives(hand)
        types = [HandClassifier.classify(cards) for cards in result]
        fh_types = [t for t in types if t and t[0] == 6]
        self.assertGreater(len(fh_types), 0)

    def test_find_four_of_a_kind(self):
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 2)])
        result = HandFinder.find_fives(hand)
        types = [HandClassifier.classify(cards) for cards in result]
        four_types = [t for t in types if t and t[0] == 7]
        self.assertGreater(len(four_types), 0)

    def test_find_straight_flush(self):
        hand = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0), Card(14, 3)])
        result = HandFinder.find_fives(hand)
        types = [HandClassifier.classify(cards) for cards in result]
        sf_types = [t for t in types if t and t[0] == 8]
        self.assertGreater(len(sf_types), 0)


class TestGetAllValidPlays(unittest.TestCase):

    def test_first_turn(self):
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        result = HandFinder.get_all_valid_plays(hand, None)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0].rank, 3)
        self.assertEqual(result[0][0].suit, 0)

    def test_with_last_single(self):
        hand = Hand([Card(5, 3), Card(6, 2), Card(14, 3)])
        last_play = [Card(5, 1)]
        result = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertGreater(len(result), 0)
        for play in result:
            self.assertEqual(len(play), 1)

    def test_with_last_pair(self):
        hand = Hand([Card(5, 3), Card(5, 2), Card(6, 3), Card(6, 2)])
        last_play = [Card(5, 1), Card(5, 0)]
        result = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertGreater(len(result), 0)
        for play in result:
            self.assertEqual(len(play), 2)

    def test_no_valid(self):
        hand = Hand([Card(3, 0), Card(4, 1)])
        last_play = [Card(14, 3)]
        result = HandFinder.get_all_valid_plays(hand, last_play)
        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()
