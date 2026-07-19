from pieces import Piece
import pygame

class King(Piece):
    SPRITE_PATH = "sprites/King_paint.png"

    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load(self.SPRITE_PATH).convert_alpha()

    def get_legal_moves(self, row, col, board):
        candidates = [
            (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1),
        ]

        legal = []
        for r, c in candidates:
            if board.in_bounds(r, c) and board.is_empty_square(r, c):
                legal.append((r, c))

        return legal