from typing import List, Optional, Tuple

from game.models import Deck, Player, Card
from game.classifier import HandClassifier


class BigTwoGame:
    def __init__(self):
        self.deck = None
        self.players: List[Player] = []
        self.current_player: int = 0
        self.last_play: Optional[Tuple[List[Card], str]] = None
        self.pass_count: int = 0
        self.winner: Optional[Player] = None
        self.round_number: int = 1

    def setup(self) -> None:
        self.deck = Deck()
        self.deck.shuffle()

        self.players = [
            Player("Human", is_ai=False),
            Player("AI-1", is_ai=True),
            Player("AI-2", is_ai=True),
            Player("AI-3", is_ai=True),
        ]

        for player in self.players:
            player.take_cards(self.deck.deal(13))

        for i, player in enumerate(self.players):
            three_clubs = player.hand.find_3_clubs()
            if three_clubs:
                self.current_player = i
                break

        self.last_play = None
        self.pass_count = 0
        self.winner = None
        self.round_number = 1

    def play(self, player: Player, cards: List[Card]) -> bool:
        if not self._is_valid_play(cards):
            return False

        player.hand.remove(cards)

        self.last_play = (cards, self._get_play_type(cards))
        self.pass_count = 0
        self.winner = self.check_winner()
        return True

    def pass_(self, player: Player) -> bool:
        self.pass_count += 1
        return True

    def next_turn(self) -> None:
        self.current_player = (self.current_player + 1) % 4

    def _is_valid_play(self, cards: List[Card]) -> bool:
        last_cards = self.last_play[0] if self.last_play else None
        return HandClassifier.can_play(last_cards, cards)

    def check_round_reset(self) -> None:
        if self.pass_count >= 3:
            self.last_play = None
            self.pass_count = 0

    def check_winner(self) -> Optional[Player]:
        for player in self.players:
            if len(player.hand) == 0:
                self.winner = player
                return player
        return None

    def is_game_over(self) -> bool:
        return self.winner is not None

    def get_current_player(self) -> Player:
        return self.players[self.current_player]

    def ai_turn(self) -> bool:
        player = self.get_current_player()
        cards = player.choose_play(self.last_play) if hasattr(player, "choose_play") else []

        if cards:
            return self.play(player, cards)
        return self.pass_(player)

    def _get_play_type(self, cards: List[Card]) -> str:
        if len(cards) == 1:
            return "single"
        if len(cards) == 2:
            return "pair"
        if len(cards) == 3:
            return "triple"
        if len(cards) == 5:
            return "five_card"
        return "unknown"
