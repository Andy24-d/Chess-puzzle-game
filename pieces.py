# Chess pieces abstract class

from __future__ import annotations
from abc import ABC, abstractmethod
import pygame

class Piece(ABC):
    def __init__(self):
        self.sprite = None

    @abstractmethod
    def get_legal_moves(self, row: int, col: int, board) -> list[tuple[int, int]]:
        """
        Devuelve una lista de coordenadas destino válidas [(r, c), ...]
        según reglas de la pieza y estado del board.
        """
        raise NotImplementedError

    # for pieces moving in straight lines
    def get_legal_moves_from_move_directions (self, row: int, col: int, board, directions: list[tuple[int, int]]) -> list[tuple[int, int]]:
        legal_moves = []
        for dir in directions:
            #Relative movement done from starting position
            move_pos = (row + dir[0], col + dir[1])
            while board.in_bounds_pos(move_pos):
                if board.is_empty_square_pos(move_pos):
                    legal_moves.append(move_pos)
                else:
                    break

                move_pos = (move_pos[0] + dir[0], move_pos[1] + dir[1])

        return legal_moves

    def draw(self, screen, cell_rect):
        if self.sprite is None:
            return
        margin = int(min(cell_rect.width, cell_rect.height) * 0.12)
        w = cell_rect.width - margin * 2
        h = cell_rect.height - margin * 2
        img = pygame.transform.smoothscale(self.sprite, (w, h))
        screen.blit(img, img.get_rect(center=cell_rect.center))