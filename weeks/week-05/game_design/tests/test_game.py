import unittest
from game.game import BigTwoGame
from game.models import Card


class TestBigTwoGame(unittest.TestCase):

    def setUp(self):
        self.game = BigTwoGame()

    def test_game_has_4_players(self):
        self.game.setup()
        self.assertEqual(len(self.game.players), 4)

    def test_each_player_13_cards(self):
        self.game.setup()
        for player in self.game.players:
            self.assertEqual(len(player.hand), 13)

    def test_total_cards_distributed(self):
        self.game.setup()
        total_cards = sum(len(player.hand) for player in self.game.players)
        self.assertEqual(total_cards, 52)

    def test_first_player_has_3_clubs(self):
        self.game.setup()
        first_player = self.game.players[self.game.current_player]
        three_clubs = first_player.hand.find_3_clubs()
        self.assertIsNotNone(three_clubs)

    def test_one_human_three_ai(self):
        self.game.setup()
        human_count = sum(1 for p in self.game.players if not p.is_ai)
        ai_count = sum(1 for p in self.game.players if p.is_ai)
        self.assertEqual(human_count, 1)
        self.assertEqual(ai_count, 3)

    def test_play_removes_cards(self):
        self.game.setup()
        player = self.game.players[self.game.current_player]
        initial_count = len(player.hand)
        three_clubs = player.hand.find_3_clubs()
        cards = [three_clubs]
        self.game.play(player, cards)
        self.assertEqual(len(player.hand), initial_count - 1)

    def test_play_sets_last_play(self):
        self.game.setup()
        player = self.game.players[self.game.current_player]
        three_clubs = player.hand.find_3_clubs()
        self.assertIsNotNone(three_clubs)
        cards = [three_clubs]
        self.game.play(player, cards)
        self.assertIsNotNone(self.game.last_play)

    def test_invalid_play(self):
        self.game.setup()
        player = self.game.players[0]
        # Try to play a card that's not 3♣ first
        cards = [card for card in player.hand if card.rank != 3 or card.suit != 0][:1]
        result = self.game.play(player, cards)
        self.assertFalse(result)

    def test_pass_increments(self):
        self.game.setup()
        initial_pass = self.game.pass_count
        player = self.game.players[0]
        self.game.pass_(player)
        self.assertEqual(self.game.pass_count, initial_pass + 1)

    def test_three_passes_resets(self):
        self.game.setup()
        player = self.game.players[self.game.current_player]
        three_clubs = player.hand.find_3_clubs()
        self.game.play(player, [three_clubs])
        for _ in range(3):
            self.game.pass_(self.game.players[1])
        self.game.check_round_reset()
        self.assertIsNone(self.game.last_play)

    def test_turn_rotates(self):
        self.game.setup()
        initial = self.game.current_player
        self.game.next_turn()
        self.assertEqual(self.game.current_player, (initial + 1) % 4)

    def test_is_game_over_no_winner(self):
        self.game.setup()
        self.assertFalse(self.game.is_game_over())

    def test_get_current_player(self):
        self.game.setup()
        player = self.game.get_current_player()
        self.assertEqual(player, self.game.players[self.game.current_player])

    def test_ai_turn_pass(self):
        self.game.setup()
        # AI player without choose_play method
        result = self.game.ai_turn()
        self.assertTrue(result)  # pass returns True

    def test_get_play_type(self):
        self.game.setup()
        player = self.game.players[self.game.current_player]
        three_clubs = player.hand.find_3_clubs()
        play_type = self.game._get_play_type([three_clubs])
        self.assertEqual(play_type, "single")

        # Test pair
        pair_cards = [card for card in player.hand if card.rank == 4][:2]
        if len(pair_cards) == 2:
            play_type = self.game._get_play_type(pair_cards)
            self.assertEqual(play_type, "pair")

        # Test five card
        five_cards = player.hand[:5]
        play_type = self.game._get_play_type(five_cards)
        self.assertEqual(play_type, "five_card")
