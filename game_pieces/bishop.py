from pieces import Piece
import pygame

class Bishop(Piece):
    SPRITE_PATH = "sprites/Bishop_paint.png"
    DIRECTIONS = [
            (1, 1),    # down-right
            (1, -1),   # down-left
            (-1, 1),   # up-right
            (-1, -1),  # up-left
        ]


    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load(self.SPRITE_PATH).convert_alpha()

    def get_legal_moves(self, row, col, board):
        return self.get_legal_moves_from_move_directions(row, col, board, self.DIRECTIONS)