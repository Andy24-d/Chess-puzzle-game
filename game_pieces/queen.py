from pieces import Piece
import pygame

class Queen(Piece):

    SPRITE_PATH = "sprites/Queen_paint.png"
    #Board grid legal movement directions
    DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load(self.SPRITE_PATH).convert_alpha()

    def get_legal_moves(self, row, col, board):
        legal = self.get_legal_moves_from_move_directions(row, col, board, self.DIRECTIONS)
        return legal