# BOARD CLASS
# Description:
#   Cells collection.

# States:
#   Locked: Can't move pieces (analysis phase)
#   Idle: Can move pieces (standard state in game)
#   Piece_selected: Whenever a piece is clicked. After it's moved or deselected it goes back to idle



import pygame
from square import Square, SquareState

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.rows = 3
        self.cols = 3

        self.screen_height  = screen.get_height()
        self.screen_width = screen.get_width()

        # Board dimensions (640x640)
        self.board_size = 640
        self.cell_size = self.board_size // 3

        # Offsets calc
        self.offset_x = 40
        self.offset_y = (self.screen_height - self.board_size) // 2  # Da 40

        # pygame.Rect (board coordinates)
        self.rect = pygame.Rect(self.offset_x, self.offset_y, self.board_size, self.board_size)

        # Grid list
        self.grid = self.make_grid()

        # Colors
        self.border_color = (139, 69, 19)  # Marrón oscuro para el borde exterior
        self.bg_color = (222, 184, 135)  # Color madera clara para el fondo
        self.line_color = (101, 67, 33)  # Marrón oscuro para las divisiones 3x3

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

    def add_piece(self, piece, row, col):
        self.grid[row][col].put_piece(piece)

    # def get_cell_from_pos(self, pos):

    def is_empty_square(self, row, col):
        return self.grid[row][col].is_empty() == True

    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_empty_square_pos(self, pos):
        return self.is_empty_square(pos[0], pos[1])

    def in_bounds_pos(self, pos):
        return self.in_bounds(pos[0], pos[1])

    def draw(self):

        # Crear el rectángulo base que define toda el área del tablero


        # Dibujar las casillas de la grilla 3x3
        for row in range(3):
            for col in range(3):
                self.grid[row][col].draw(self.screen)

        # Dibujar el borde exterior grueso
        # Pasar un número mayor a 0 en el cuarto parámetro dibuja solo el borde
        pygame.draw.rect(self.screen, self.border_color, self.rect, self.border_thickness)







