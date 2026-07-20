# Board's Cells. Cells store a single piece each.
# Render State:
#   Normal
#   Highlighted
#   Selectable

import pygame
from enum import Enum, auto

class SquareState(Enum):
    NORMAL = auto()
    HIGHLIGHTED = auto()
    SELECTABLE = auto()

class Square:
    GRID_SIZE = 3  # tablero 3x3

    # Class constants
    HIGHLIGHT_COLOR = (243, 248, 86)
    SELECTABLE_GREEN = (34, 177, 76)
    SELECTABLE_ALPHA = 140  # ~55% opacity (255 * 0.55 ≈ 140)

    def __init__(self, row, col, board_rect, dark, light, piece=None):
        self.row = row
        self.col = col
        self.board_rect = board_rect  # pygame.Rect of the board the square is in
        self.piece = piece
        self.state = SquareState.NORMAL

        self.bg_dark = dark
        self.bg_light = light

        # tamaño de casilla
        self.cell_w = self.board_rect.width // self.GRID_SIZE
        self.cell_h = self.board_rect.height // self.GRID_SIZE

        # rect de esta casilla
        x = self.board_rect.left + self.col * self.cell_w
        y = self.board_rect.top + self.row * self.cell_h
        self.rect = pygame.Rect(x, y, self.cell_w, self.cell_h)

        def __eq__(self, other):
            if not isinstance(other, Square):
                print("NotImplemented")
                return NotImplemented

            if self.row != other.row or self.col != other.col:
                print("Different positions")
                return False

            if self.is_empty() == other.is_empty():
                print("Empty state:" + str(self.is_empty()))
                print("piece eq:" + str(self.piece == other.piece))
                return self.is_empty() or ( self.piece == other.piece )
            else:
                print("Different empty states")
                return False

    def put_piece(self, piece):
        self.piece = piece

    def get_piece(self):
        return self.piece

    def take_piece(self):
        removed = self.piece
        self.piece = None
        return removed

    def is_occupied(self):
        return self.piece is not None

    def is_empty(self):
        return self.piece is None

    def set_state(self, state):
        self.state = state

    def reset_state(self):
        self.state = SquareState.NORMAL

    def contains_point(self, pos):
        return self.rect.collidepoint(pos)

    def center(self):
        return self.rect.center

    def draw(self, screen):
        # 1) Background color logic
        if self.state == SquareState.HIGHLIGHTED:
            bg_color = self.HIGHLIGHT_COLOR
        else:
            # NORMAL o SELECTABLE -> patrón ajedrez
            is_dark = (self.row + self.col) % 2 == 0  # (0,0) dark
            bg_color = self.bg_dark if is_dark else self.bg_light

        pygame.draw.rect(screen, bg_color, self.rect)

        # 2) Piece render
        if self.is_occupied():
            self.piece.draw(screen, self.rect)

        # 3) Selectable indicator (green dot)
        if self.state == SquareState.SELECTABLE:
            radius = int(min(self.rect.width, self.rect.height) * 0.14)

            # Surface temporal con alpha para el círculo
            overlay = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
            circle_color = (*self.SELECTABLE_GREEN, self.SELECTABLE_ALPHA)
            center_local = (self.rect.width // 2, self.rect.height // 2)

            pygame.draw.circle(overlay, circle_color, center_local, radius)
            screen.blit(overlay, self.rect.topleft)