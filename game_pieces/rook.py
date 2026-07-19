from pieces import Piece
import pygame

class Rook(Piece):
    SPRITE_PATH = "sprites/Rook_paint.png"
    DIRECTIONS = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1),  # left
        ]

    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load(self.SPRITE_PATH).convert_alpha()

    def get_legal_moves(self, row, col, board):
        return self.get_legal_moves_from_move_directions(row, col, board, self.DIRECTIONS)