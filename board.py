# BOARD CLASS
# Description:
#   Cells collection.

# States:
#   Locked: Can't move pieces (analysis phase)
#   Unlocked: Can move pieces (standard state in game)
#   Piece_selected: Whenever a piece is clicked. After it's moved or deselected it goes back to unlocked

# Render order (back to front):
#   1. Board background
#       a. draw cells
#       b. draw board border
#   2. Effects (Selection highlights)
#   3. Pieces

import pygame
from square import Square, SquareState

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.rows = 3
        self.cols = 3

        # Ajustes visuales
        self.screen_height  = screen.get_height()
        self.screen_width = screen.get_width()

        # Tamaño del tablero (640x640)
        self.board_size = 640
        self.cell_size = self.board_size // 3

        # Cálculo de los offsets (distancia a los márgenes)
        self.offset_x = 40
        self.offset_y = (self.screen_height - self.board_size) // 2  # Da 40

        # Rectangulo que representa coordenas del tablero
        self.rect = pygame.Rect(self.offset_x, self.offset_y, self.board_size, self.board_size)

        print(type(self.rect), self.rect)
        square = Square(0, 0, self.rect)
        print(type(square.rect), square.rect)

        # Lista de la grilla
        self.grid = self.make_grid()

        # Colores (Inspirados en la madera de tu imagen)
        self.border_color = (139, 69, 19)  # Marrón oscuro para el borde exterior
        self.bg_color = (222, 184, 135)  # Color madera clara para el fondo
        self.line_color = (101, 67, 33)  # Marrón oscuro para las divisiones 3x3

        # Grosor del borde exterior
        self.border_thickness = 12

    def make_grid(self):
        grid = []
        for row in range(self.rows):
            row_list = []
            for col in range(self.cols):
                empty_square = Square(row, col, self.rect)
                row_list.append(empty_square)

            grid.append(row_list)
        return grid

    def draw(self):

        # Crear el rectángulo base que define toda el área del tablero


        # Dibujar las casillas de la grilla 3x3
        for row in range(3):
            for col in range(3):
                self.grid[row][col].draw(self.screen)

        # Dibujar el borde exterior grueso
        # Pasar un número mayor a 0 en el cuarto parámetro dibuja solo el borde
        pygame.draw.rect(self.screen, self.border_color, self.rect, self.border_thickness)



    def get_cell_from_pos(self, pos):
        """Convierte una coordenada (x, y) de ratón en índices (fila, columna)."""
        x, y = pos
        row = y // self.cell_size
        col = x // self.cell_size
        return row, col



