import unittest
from game.models import Card, Deck, Hand, Player


class TestCard(unittest.TestCase):

    def test_card_creation(self):
        card = Card(rank=14, suit=3)
        self.assertEqual(card.rank, 14)
        self.assertEqual(card.suit, 3)

    def test_card_repr_ace(self):
        card = Card(14, 3)
        self.assertEqual(repr(card), "♠A")

    def test_card_repr_three(self):
        card = Card(3, 0)
        self.assertEqual(repr(card), "♣3")

    def test_card_compare_suit(self):
        card1 = Card(14, 3)
        card2 = Card(14, 2)
        self.assertTrue(card1 > card2)

    def test_card_compare_suit_2(self):
        card1 = Card(14, 2)
        card2 = Card(14, 1)
        self.assertTrue(card1 > card2)

    def test_card_compare_suit_3(self):
        card1 = Card(14, 1)
        card2 = Card(14, 0)
        self.assertTrue(card1 > card2)

    def test_card_compare_rank_2(self):
        card1 = Card(15, 0)
        card2 = Card(14, 3)
        self.assertTrue(card1 > card2)

    def test_card_compare_rank_a(self):
        card1 = Card(14, 0)
        card2 = Card(13, 3)
        self.assertTrue(card1 > card2)

    def test_card_compare_equal(self):
        card1 = Card(14, 3)
        card2 = Card(14, 3)
        self.assertFalse(card1 > card2)

    def test_card_sort_key(self):
        card = Card(14, 3)
        self.assertEqual(card.to_sort_key(), (14, 3))


class TestDeck(unittest.TestCase):

    def test_deck_has_52_cards(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_all_unique(self):
        deck = Deck()
        self.assertEqual(len(set(deck.cards)), 52)

    def test_deck_all_ranks(self):
        deck = Deck()
        ranks = set(card.rank for card in deck.cards)
        self.assertEqual(ranks, set(range(3, 16)))

    def test_deck_all_suits(self):
        deck = Deck()
        suits = set(card.suit for card in deck.cards)
        self.assertEqual(suits, {0, 1, 2, 3})

    def test_deck_shuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck2.shuffle()
        self.assertNotEqual(
            [card.to_sort_key() for card in deck1.cards],
            [card.to_sort_key() for card in deck2.cards]
        )

    def test_deal_5_cards(self):
        deck = Deck()
        dealt = deck.deal(5)
        self.assertEqual(len(dealt), 5)
        self.assertEqual(len(deck.cards), 47)

    def test_deal_multiple(self):
        deck = Deck()
        deck.deal(5)
        deck.deal(3)
        self.assertEqual(len(deck.cards), 44)

    def test_deal_exceed(self):
        deck = Deck()
        dealt = deck.deal(60)
        self.assertEqual(len(dealt), 52)
        self.assertEqual(len(deck.cards), 0)


class TestHand(unittest.TestCase):

    def test_hand_creation(self):
        cards = [Card(3, 0), Card(4, 1), Card(5, 2)]
        hand = Hand(cards)
        self.assertEqual(len(hand), 3)

    def test_hand_sort_desc(self):
        cards = [Card(3, 0), Card(14, 3), Card(3, 3), Card(13, 2)]
        hand = Hand(cards)
        hand.sort_desc()
        sorted_ranks = [card.rank for card in hand]
        self.assertEqual(sorted_ranks, [14, 13, 3, 3])

    def test_hand_find_3_clubs(self):
        cards = [Card(14, 3), Card(3, 0), Card(3, 1)]
        hand = Hand(cards)
        result = hand.find_3_clubs()
        self.assertIsNotNone(result)
        self.assertEqual(result.rank, 3)
        self.assertEqual(result.suit, 0)

    def test_hand_find_3_clubs_none(self):
        cards = [Card(14, 3), Card(3, 1)]
        hand = Hand(cards)
        result = hand.find_3_clubs()
        self.assertIsNone(result)

    def test_hand_remove(self):
        cards = [Card(14, 3), Card(14, 2)]
        hand = Hand(cards)
        hand.remove([Card(14, 3)])
        self.assertEqual(len(hand), 1)

    def test_hand_remove_not_found(self):
        cards = [Card(14, 3)]
        hand = Hand(cards)
        hand.remove([Card(14, 2)])
        self.assertEqual(len(hand), 1)

    def test_hand_iteration(self):
        cards = [Card(14, 3), Card(14, 2)]
        hand = Hand(cards)
        self.assertEqual(len(list(hand)), 2)


class TestPlayer(unittest.TestCase):

    def test_player_human(self):
        player = Player("Player1", False)
        self.assertFalse(player.is_ai)

    def test_player_ai(self):
        player = Player("AI_1", True)
        self.assertTrue(player.is_ai)

    def test_player_take(self):
        player = Player("Player1")
        cards = [Card(14, 3), Card(14, 2)]
        player.take_cards(cards)
        self.assertEqual(len(player.hand), 2)

    def test_player_play(self):
        player = Player("Player1")
        cards = [Card(14, 3), Card(14, 2)]
        player.take_cards(cards)
        played = player.play_cards([Card(14, 3)])
        self.assertEqual(len(played), 1)
        self.assertEqual(len(player.hand), 1)


if __name__ == "__main__":
    unittest.main()
