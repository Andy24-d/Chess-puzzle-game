from pieces import Piece
import pygame

class Knight(Piece):

    SPRITE_PATH = "sprites/Knight_paint.png"

    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load(self.SPRITE_PATH).convert_alpha()

    def get_legal_moves(self, row, col, board):
        candidates = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2),
        ]

        legal = []
        for r, c in candidates:
            if board.in_bounds(r, c):
                # ajusta esta parte a tus reglas de captura/ocupación
                if board.is_empty(r, c):
                    legal.append((r, c))
        return legal