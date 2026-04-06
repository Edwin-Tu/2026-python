import pygame
from typing import List, Dict, Optional
from game.models import Card, Player, Hand


class Renderer:
    COLORS = {
        'background': (45, 45, 45),
        'card_back': (74, 144, 217),
        'spade_club': (0, 0, 0),
        'heart_diamond': (231, 76, 60),
        'player': (46, 204, 113),
        'ai': (149, 165, 166),
        'selected': (241, 196, 15),
        'button': (52, 152, 219),
        'text': (255, 255, 255),
        'card_bg': (255, 255, 240),
    }
    SUIT_LETTERS = {
        0: 'C',
        1: 'D',
        2: 'H',
        3: 'S',
    }

    CARD_WIDTH = 60
    CARD_HEIGHT = 90
    CARD_OVERLAP = 30
    CARD_AREA_X = 50
    CARD_AREA_Y = 400
    SELECTED_OFFSET = 20
    CARD_BORDER_RADIUS = 5
    CARD_INNER_MARGIN = 5
    RANK_TEXT_OFFSET = 5
    SUIT_TEXT_OFFSET_X = 20
    SUIT_TEXT_OFFSET_Y = 25

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 24)
        self.large_font = pygame.font.SysFont('Arial', 36, bold=True)

    def draw_card(self, card: Card, x: float, y: float, selected: bool = False, face_up: bool = True):
        offset_y = self.SELECTED_OFFSET if selected else 0
        rect = pygame.Rect(x, y - offset_y, self.CARD_WIDTH, self.CARD_HEIGHT)
        pygame.draw.rect(self.screen, self.COLORS['card_bg'], rect, border_radius=self.CARD_BORDER_RADIUS)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 2, border_radius=self.CARD_BORDER_RADIUS)

        if face_up:
            color = self._get_card_color(card)
            rank_text = self.font.render(card.RANK_SYMBOLS[card.rank], True, color)
            self.screen.blit(rank_text, (x + self.RANK_TEXT_OFFSET, y + self.RANK_TEXT_OFFSET - offset_y))

            suit_symbol = self._get_suit_symbol(card)
            suit_color = self._get_card_color(card)
            suit_text = self.font.render(suit_symbol, True, suit_color)
            self.screen.blit(suit_text, (x + self.CARD_WIDTH - self.SUIT_TEXT_OFFSET_X,
                                         y + self.CARD_HEIGHT - self.SUIT_TEXT_OFFSET_Y - offset_y))

            center_text = self.large_font.render(suit_symbol, True, suit_color)
            center_rect = center_text.get_rect(
                center=(x + self.CARD_WIDTH / 2, y + self.CARD_HEIGHT / 2 - offset_y)
            )
            self.screen.blit(center_text, center_rect)
        else:
            inner_rect = pygame.Rect(x + self.CARD_INNER_MARGIN, y + self.CARD_INNER_MARGIN - offset_y,
                                     self.CARD_WIDTH - 2 * self.CARD_INNER_MARGIN,
                                     self.CARD_HEIGHT - 2 * self.CARD_INNER_MARGIN)
            pygame.draw.rect(self.screen, self.COLORS['card_back'], inner_rect, border_radius=3)

    def _get_card_color(self, card: Card) -> tuple:
        """Return the appropriate color for card text based on suit."""
        if card.suit in (0, 3):
            return (0, 0, 0)
        return self.COLORS['heart_diamond']

    def _get_suit_symbol(self, card: Card) -> str:
        """Return a suit symbol or letter fallback."""
        symbol = card.SUIT_SYMBOLS.get(card.suit, '')
        if symbol:
            return symbol
        return self.SUIT_LETTERS.get(card.suit, '?')

    def draw_hand(self, hand: Hand, x: float, y: float, selected_indices: List[int], face_up: bool = True):
        for i, card in enumerate(hand):
            card_x = x + i * self.CARD_OVERLAP
            self.draw_card(card, card_x, y, selected=i in selected_indices, face_up=face_up)

    def draw_player(self, player: Player, x: float, y: float, is_current: bool):
        color = self.COLORS['player'] if not player.is_ai else self.COLORS['ai']
        if is_current:
            pygame.draw.circle(self.screen, self.COLORS['selected'], (x + 50, y), 5)
        text = self.font.render(f"{player.name} ({len(player.hand)})", True, color)
        self.screen.blit(text, (x, y))

    def draw_last_play(self, cards: Optional[List[Card]], player_name: Optional[str], x: float, y: float):
        if player_name:
            label = self.font.render(f"{player_name} played:", True, self.COLORS['text'])
            self.screen.blit(label, (x, y))
            y += 25
        if cards:
            for i, card in enumerate(cards):
                self.draw_card(card, x + i * 35, y, face_up=True)

    def draw_buttons(self, buttons: Dict, x: float, y: float):
        for name, (btn_x, btn_y, width, height) in buttons.items():
            pygame.draw.rect(self.screen, self.COLORS['button'],
                             (x + btn_x, y + btn_y, width, height), border_radius=5)
            text = self.font.render(name, True, self.COLORS['text'])
            text_rect = text.get_rect(center=(x + btn_x + width // 2, y + btn_y + height // 2))
            self.screen.blit(text, text_rect)

    def draw_background(self):
        self.screen.fill(self.COLORS['background'])

    def draw_game_over(self, winner_name: str):
        overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        text = self.large_font.render(f"{winner_name} Wins!", True, self.COLORS['selected'])
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)
