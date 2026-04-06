import pygame
from typing import List, Tuple, Dict
from game.game import BigTwoGame
from ui.render import Renderer


class InputHandler:
    CARD_AREA_Y = 400
    CARD_AREA_X = 50
    CARD_OVERLAP = 30
    CARD_HEIGHT = 90

    def __init__(self, renderer: Renderer, buttons: Dict):
        self.renderer = renderer
        self.selected_indices: List[int] = []
        self.buttons = buttons

    def handle_event(self, event: pygame.event.Event, game: BigTwoGame) -> bool:
        """Handle pygame events and return True if game state changed."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.handle_click(event.pos, game)
        elif event.type == pygame.KEYDOWN:
            return self.handle_key(event.key, game)
        return False

    def handle_click(self, pos: Tuple[int, int], game: BigTwoGame) -> bool:
        """Handle mouse click events."""
        x, y = pos
        player = game.get_current_player()
        if player.is_ai:
            return False

        # Check button clicks first
        if self._check_button_click(x, y, game):
            return True

        # Check card selection
        return self._check_card_selection(x, y, player)

    def _check_button_click(self, x: int, y: int, game: BigTwoGame) -> bool:
        """Check if a button was clicked."""
        for name, (btn_x, btn_y, width, height) in self.buttons.items():
            if btn_x <= x <= btn_x + width and btn_y <= y <= btn_y + height:
                return self._handle_button_click(name, game)
        return False

    def _check_card_selection(self, x: int, y: int, player) -> bool:
        """Check if a card was selected."""
        if not (self.CARD_AREA_Y <= y <= self.CARD_AREA_Y + self.CARD_HEIGHT):
            return False

        card_index = (x - self.CARD_AREA_X) // self.CARD_OVERLAP
        if not (0 <= card_index < len(player.hand)):
            return False

        # Toggle selection
        if card_index in self.selected_indices:
            self.selected_indices.remove(card_index)
        else:
            self.selected_indices.append(card_index)
        return True

    def _handle_button_click(self, name: str, game: BigTwoGame) -> bool:
        if name == "Play" and self.selected_indices:
            return self.try_play(game)
        elif name == "Pass":
            return self.try_pass(game)
        return False

    def handle_key(self, key: int, game: BigTwoGame) -> bool:
        if key == pygame.K_RETURN:
            return self.try_play(game)
        elif key in (pygame.K_p, pygame.K_CAPSLOCK):
            return self.try_pass(game)
        return False

    def try_play(self, game: BigTwoGame) -> bool:
        player = game.get_current_player()
        if player.is_ai:
            return False
        if not self.selected_indices:
            return False

        cards = [player.hand[i] for i in sorted(self.selected_indices)]
        if game.play(player, cards):
            self.selected_indices = []
            return True
        return False

    def try_pass(self, game: BigTwoGame) -> bool:
        player = game.get_current_player()
        if player.is_ai:
            return False
        if game.last_play is None:
            return False
        game.pass_(player)
        return True

    def clear_selection(self):
        self.selected_indices = []
