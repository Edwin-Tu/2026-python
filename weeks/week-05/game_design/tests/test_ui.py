import unittest
from unittest.mock import Mock, MagicMock, patch
import sys

sys.modules['pygame'] = Mock()

from game.game import BigTwoGame
from game.models import Card, Player, Hand
from ui.render import Renderer
from ui.input import InputHandler


class TestRenderer(unittest.TestCase):

    def setUp(self):
        self.mock_screen = Mock()
        self.mock_screen.get_width.return_value = 800
        self.mock_screen.get_height.return_value = 600
        self.renderer = Renderer(self.mock_screen)

    def test_renderer_initialized(self):
        self.assertIsNotNone(self.renderer)
        self.assertIsNotNone(self.renderer.COLORS)

    def test_card_render_colors(self):
        black_card = Card(14, 3)
        self.assertEqual(self.renderer._get_card_color(black_card), (0, 0, 0))

        red_card = Card(14, 1)
        self.assertEqual(self.renderer._get_card_color(red_card), (231, 76, 60))

    def test_colors_defined(self):
        self.assertIn('background', self.renderer.COLORS)
        self.assertIn('card_back', self.renderer.COLORS)
        self.assertIn('player', self.renderer.COLORS)
        self.assertIn('ai', self.renderer.COLORS)

    def test_card_dimensions(self):
        self.assertEqual(self.renderer.CARD_WIDTH, 60)
        self.assertEqual(self.renderer.CARD_HEIGHT, 90)
        self.assertEqual(self.renderer.CARD_OVERLAP, 30)

    def test_card_area_coords(self):
        self.assertEqual(self.renderer.CARD_AREA_X, 50)
        self.assertEqual(self.renderer.CARD_AREA_Y, 400)


class TestInputHandler(unittest.TestCase):

    def setUp(self):
        self.mock_renderer = Mock()
        self.buttons = {
            "Play": (650, 520, 80, 35),
            "Pass": (550, 520, 80, 35),
        }
        self.input_handler = InputHandler(self.mock_renderer, self.buttons)

    def test_input_handler_initialized(self):
        self.assertIsNotNone(self.input_handler)
        self.assertEqual(self.input_handler.selected_indices, [])

    def test_select_card(self):
        mock_game = Mock()
        mock_player = Mock()
        mock_player.is_ai = False
        mock_player.hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2)])
        mock_game.get_current_player.return_value = mock_player

        self.input_handler.handle_click((100, 450), mock_game)
        self.assertIn(1, self.input_handler.selected_indices)

    def test_deselect_card(self):
        self.input_handler.selected_indices = [0, 1, 2]
        mock_game = Mock()
        mock_player = Mock()
        mock_player.is_ai = False
        mock_player.hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2)])
        mock_game.get_current_player.return_value = mock_player

        self.input_handler.handle_click((70, 450), mock_game)
        self.assertNotIn(0, self.input_handler.selected_indices)

    def test_button_click_play(self):
        mock_game = Mock()
        mock_player = Mock()
        mock_player.is_ai = False
        mock_player.hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2)])
        mock_game.get_current_player.return_value = mock_player
        mock_game.play.return_value = True

        self.input_handler.selected_indices = [0]

        result = self.input_handler._handle_button_click("Play", mock_game)
        self.assertTrue(result)
        self.assertEqual(self.input_handler.selected_indices, [])

    def test_button_click_pass(self):
        mock_game = Mock()
        mock_game.last_play = [Card(3, 0)]
        mock_player = Mock()
        mock_player.is_ai = False
        mock_game.get_current_player.return_value = mock_player

        result = self.input_handler._handle_button_click("Pass", mock_game)
        self.assertTrue(result)

    def test_clear_selection(self):
        self.input_handler.selected_indices = [0, 1, 2]
        self.input_handler.clear_selection()
        self.assertEqual(self.input_handler.selected_indices, [])

    def test_ai_ignores_input(self):
        mock_game = Mock()
        mock_player = Mock()
        mock_player.is_ai = True
        mock_game.get_current_player.return_value = mock_player

        result = self.input_handler.handle_click((100, 450), mock_game)
        self.assertFalse(result)


class TestUIIntegration(unittest.TestCase):

    def test_game_init_creates_4_players(self):
        game = BigTwoGame()
        game.setup()
        self.assertEqual(len(game.players), 4)

    def test_card_selection_converts_coordinates(self):
        mock_renderer = Mock()
        buttons = {"Play": (650, 520, 80, 35)}
        handler = InputHandler(mock_renderer, buttons)

        mock_game = Mock()
        mock_player = Mock()
        mock_player.is_ai = False
        mock_player.hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2)])
        mock_game.get_current_player.return_value = mock_player

        x = 50 + 1 * 30
        handler.handle_click((x, 450), mock_game)
        self.assertIn(1, handler.selected_indices)

    def test_buttons_defined(self):
        buttons = {
            "Play": (650, 520, 80, 35),
            "Pass": (550, 520, 80, 35),
        }
        self.assertIn("Play", buttons)
        self.assertIn("Pass", buttons)
        self.assertEqual(buttons["Play"][2], 80)
        self.assertEqual(buttons["Play"][3], 35)


if __name__ == '__main__':
    unittest.main()
