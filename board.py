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
import Cell from cell

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.rows = 3
        self.cols = 3
        # Representación lógica: 0 = vacío, o podrías guardar objetos 'Piece'
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        # Ajustes visuales
        self.screen_height  = screen.get_height()
        self.screen_width = screen.get_width()

        # Tamaño del tablero (640x640)
        self.board_size = 640
        self.cell_size = self.board_size // 3

        # Cálculo de los offsets (distancia a los márgenes)
        self.offset_x = 40
        self.offset_y = (self.screen_height - self.board_size) // 2  # Da 40

        # Colores (Inspirados en la madera de tu imagen)
        self.border_color = (139, 69, 19)  # Marrón oscuro para el borde exterior
        self.bg_color = (222, 184, 135)  # Color madera clara para el fondo
        self.line_color = (101, 67, 33)  # Marrón oscuro para las divisiones 3x3

        # Grosor del borde exterior
        self.border_thickness = 12

    def draw(self):

        # Crear el rectángulo base que define toda el área del tablero
        board_rect = pygame.Rect(self.offset_x, self.offset_y, self.board_size, self.board_size)

        # Dibujar el fondo del tablero
        pygame.draw.rect(self.screen, self.bg_color, board_rect)

        # Dibujar las líneas de la grilla 3x3 (las divisiones internas)

        for i in range(1, 3):
            # Coordenadas para las líneas verticales
            start_pos_v = (self.offset_x + i * self.cell_size, self.offset_y)
            end_pos_v = (self.offset_x + i * self.cell_size, self.offset_y + self.board_size - self.border_thickness)
            pygame.draw.line(self.screen, self.line_color, start_pos_v, end_pos_v, 4)

            # Coordenadas para las líneas horizontales
            start_pos_h = (self.offset_x, self.offset_y + i * self.cell_size)
            end_pos_h = (self.offset_x + self.board_size - self.border_thickness, self.offset_y + i * self.cell_size)
            pygame.draw.line(self.screen, self.line_color, start_pos_h, end_pos_h, 4)

        # Dibujar el borde exterior grueso
        # Pasar un número mayor a 0 en el cuarto parámetro dibuja solo el borde
        pygame.draw.rect(self.screen, self.border_color, board_rect, self.border_thickness)



    def get_cell_from_pos(self, pos):
        """Convierte una coordenada (x, y) de ratón en índices (fila, columna)."""
        x, y = pos
        row = y // self.cell_size
        col = x // self.cell_size
        return row, col



