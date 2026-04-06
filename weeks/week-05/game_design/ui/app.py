import pygame
import time
from typing import Dict
from game.game import BigTwoGame
from ui.render import Renderer
from ui.input import InputHandler


class BigTwoApp:
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BUTTON_WIDTH = 80
    BUTTON_HEIGHT = 35
    FPS = 60
    AI_DELAY = 0.5

    # Player positions: (x, y) for each player index
    PLAYER_POSITIONS = [
        (10, 10),      # Human player (bottom left)
        (10, 200),     # AI 1 (left)
        (350, 30),     # AI 2 (top)
        (650, 200),    # AI 3 (right)
    ]

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Big Two - Phase 6")
        self.renderer = Renderer(self.screen)
        self.game = BigTwoGame()
        self.game.setup()
        self.buttons = self._create_buttons()
        self.input_handler = InputHandler(self.renderer, self.buttons)
        self.clock = pygame.time.Clock()

    def _create_buttons(self) -> Dict:
        return {
            "Play": (650, 520, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
            "Pass": (550, 520, self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
        }

    def run(self):
        """Main game loop."""
        running = True
        while running:
            running = self._handle_events()
            self._update_game_state()
            self._check_game_end()
            self.render()
            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()

    def _handle_events(self) -> bool:
        """Handle pygame events. Return False to quit."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
            elif not self.game.is_game_over():
                self.input_handler.handle_event(event, self.game)
        return True

    def _update_game_state(self):
        """Update game state for AI turns."""
        if self.game.is_game_over():
            return

        current_player = self.game.get_current_player()
        if current_player.is_ai:
            time.sleep(self.AI_DELAY)
            self.game.ai_turn()
            self.game.next_turn()
            self.game.check_round_reset()
            self.game.check_winner()

    def _check_game_end(self):
        """Check if game should end."""
        if self.game.is_game_over():
            time.sleep(2)  # Show winner for 2 seconds

    def render(self):
        """Render the complete game state."""
        self.renderer.draw_background()
        self._render_players()
        self._render_hands()
        self._render_last_play()
        self._render_ui()
        self._render_game_status()

    def _render_players(self):
        """Render all player information."""
        for i, player in enumerate(self.game.players):
            x, y = self.PLAYER_POSITIONS[i]
            is_current = (i == self.game.current_player)
            self.renderer.draw_player(player, x, y, is_current)

    def _render_hands(self):
        """Render all player hands."""
        # Human player (face up with selection)
        human = self.game.players[0]
        self.renderer.draw_hand(
            human.hand,
            self.renderer.CARD_AREA_X,
            self.renderer.CARD_AREA_Y,
            self.input_handler.selected_indices,
            face_up=True
        )

        # AI players (face down)
        ai_positions = [(10, 220), (300, 60), (600, 220)]
        for i, pos in enumerate(ai_positions):
            player = self.game.players[i + 1]
            self.renderer.draw_hand(player.hand, pos[0], pos[1], [], face_up=False)

    def _render_last_play(self):
        """Render the last played cards."""
        if self.game.last_play:
            cards, _ = self.game.last_play
            self.renderer.draw_last_play(cards, None, 300, 100)
        else:
            label = self.renderer.font.render("No cards played yet", True, self.renderer.COLORS['text'])
            self.screen.blit(label, (300, 100))

    def _render_ui(self):
        """Render UI elements."""
        self.renderer.draw_buttons(self.buttons, 0, 0)

    def _render_game_status(self):
        """Render current game status."""
        current = self.game.get_current_player()
        if not current.is_ai:
            status = f"Current: {current.name}"
        else:
            status = "AI thinking..."
        status_text = self.renderer.font.render(status, True, self.renderer.COLORS['text'])
        self.screen.blit(status_text, (10, 560))

        if self.game.is_game_over():
            self.renderer.draw_game_over(self.game.winner.name)
