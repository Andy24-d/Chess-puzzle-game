# BOARD CLASS
# Description:
#   Cells collection.

# States:
#   Locked: Can't move pieces (analysis phase)
#   Idle: Can move pieces (standard state in game)
#   Piece_selected: Whenever a piece is clicked. After it's moved or deselected it goes back to idle



import pygame
from square import Square, SquareState
from game_pieces import Knight, Queen, Bishop, Rook, King
import random

class Board:
    def __init__(self, screen, board_size=640, offset_x=40, offset_y=40, dark_sq=(105, 70, 30), light_sq=(211, 164, 100)):
        self.screen = screen
        self.rows = 3
        self.cols = 3

        self.screen_height  = screen.get_height()
        self.screen_width = screen.get_width()

        # Board dimensions (640x640)
        self.board_size = board_size
        self.cell_size = self.board_size // 3

        # Offsets calc
        self.offset_x = offset_x
        self.offset_y = offset_y

        # pygame.Rect (board coordinates)
        self.rect = pygame.Rect(self.offset_x, self.offset_y, self.board_size, self.board_size)

        # Grid list
        self.grid = self.make_grid(dark_sq, light_sq)

        # Colors
        self.border_color = (139, 69, 19)  # Marrón oscuro para el borde exterior

        self.border_thickness = 12

        # Board state
        self.state = Unlocked_State()
        self.selected_square_pos = (0, 0)
        self.choseable_squares_pos = []

    def __eq__(self, other):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.get_square(row, col) != other.get_square(row, col):
                    return False

        return True

    def make_grid(self, sq_dark, sq_light):
        grid = []
        for row in range(self.rows):
            row_list = []
            for col in range(self.cols):
                empty_square = Square(row, col, self.rect, dark=sq_dark, light=sq_light)
                row_list.append(empty_square)

            grid.append(row_list)

        return grid

    def setup(self):
        # 6 piezas + 3 vacías
        pool = [
            King(), Queen(), Rook(), Bishop(), Knight(), None,
            None, None, None
        ]

        random.shuffle(pool)
        #Prevents unresolvable game states where the knight is in the middle and thus it can't move anywhere
        while isinstance( pool[4], Knight ):
            random.shuffle(pool)

        for row in range(self.rows):
            for col in range(self.cols):
                piece = pool[row*3 + col]
                self.add_piece(piece, row, col)

    def setup_solvable(self, game_board):
        solvable = False
        while self != game_board and not solvable:
            self.setup()

            game_bishop_pos = game_board.find_bishop_pos()
            objective_bishop_pos = self.find_bishop_pos()
            if Board.same_color(game_bishop_pos, objective_bishop_pos):
                solvable = True

    @staticmethod
    def same_color(cell_a, cell_b):
        ra, ca = cell_a
        rb, cb = cell_b
        return (ra + ca) % 2 == (rb + cb) % 2

    def find_bishop_pos(self):
        for r in range(self.rows):
            for c in range(self.cols):
                p = self.get_square(r, c).get_piece()
                if isinstance(p, Bishop):
                    return (r, c)
        return None



    def add_piece(self, piece, row, col):
        self.grid[row][col].put_piece(piece)

    def get_piece(self, row, col):
        return self.grid[row][col].get_piece()

    def swap_pieces(self, cell1, cell2):
        #rows and cols
        r1, c1 = cell1
        r2, c2 = cell2

        piece1 = self.get_square(r1, c1).take_piece()
        piece2 = self.get_square(r2, c2).take_piece()

        self.add_piece(piece1, r2, c2)
        self.add_piece(piece2, r1, c1)

    def get_index_from_pos(self, pos):
        """
        Convert screen coordinates (x, y) into grid indices (row, col).
        Returns (row, col) or None if pos is outside board rect.
        """
        x, y = pos

        if not self.rect.collidepoint(x, y):
            return None

        col = (x - self.rect.left) // self.cell_size
        row = (y - self.rect.top)  // self.cell_size

        return (row, col)

    def is_empty_square(self, row, col):
        return self.grid[row][col].is_empty() == True

    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_empty_square_pos(self, pos):
        return self.is_empty_square(pos[0], pos[1])

    def in_bounds_pos(self, pos):
        return self.in_bounds(pos[0], pos[1])

    def get_square(self, row, col):
        return self.grid[row][col]

    def rotate_clock(self):
        new_grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                new_square = self.get_square(row, col)
                new_square.change_pos(col, self.rows - 1 - row)
                new_grid[col][self.rows - 1 - row] = new_square
        self.grid = new_grid

    def rotate_inverse(self):
        new_grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                new_square = self.get_square(row, col)
                new_square.change_pos(self.cols - 1 - col, row)
                new_grid[self.cols - 1 - col][row] = new_square
        self.grid = new_grid

    def flip_horizontal(self):
        for col in range(self.cols):
            self.swap_pieces((0, col), (self.rows - 1, col))

    def flip_vertical(self):
        for row in range(self.rows):
            self.swap_pieces((row, 0), (row, self.cols - 1))

    def draw(self):

        # Dibujar las casillas de la grilla 3x3
        for row in range(3):
            for col in range(3):
                self.grid[row][col].draw(self.screen)

        # Dibujar el borde exterior grueso
        # Pasar un número mayor a 0 en el cuarto parámetro dibuja solo el borde
        pygame.draw.rect(self.screen, self.border_color, self.rect, self.border_thickness)

    def handle_click(self, pos):
        self.state.on_click(self, pos)

    #PRE: A piece is selected
    def deselect(self):
        r, c = self.selected_square_pos
        self.get_square(r, c).reset_state()

        for row, col in self.choseable_squares_pos:
            self.get_square(row, col).reset_state()

    def select_square(self, row, col):
        self.deselect()

        self.selected_square_pos = (row, col)
        square = self.get_square(row, col)
        square.state = SquareState.HIGHLIGHTED

        self.choseable_squares_pos = square.get_piece().get_legal_moves(row, col, self)
        for row, col in self.choseable_squares_pos:
            self.get_square(row, col).state = SquareState.SELECTABLE

    def move_selected_to(self, row, col):
        self.swap_pieces(self.selected_square_pos, (row, col) )

    def lock(self):
        self.state = Locked_State()
    def unlock(self):
        self.state = Unlocked_State()

# Board state classes definitions:

from abc import ABC, abstractmethod

class BoardState(ABC):
    @abstractmethod
    def on_click(self, board, pos):
        pass

class Locked_State(BoardState):
    def on_click(self, board, pos):
        # ignore clicks
        return

class Unlocked_State(BoardState):
    def on_click(self, board, pos):
        cell_index = board.get_index_from_pos(pos)
        if cell_index is None:
            board.deselect()
            return

        row, col = cell_index
        if board.is_empty_square(row, col):
            return
        else:
            board.select_square(row, col)
            board.state = Piece_Selected_State()



class Piece_Selected_State(BoardState):
    def on_click(self, board, pos):
        cell_index = board.get_index_from_pos(pos)
        if cell_index is None:
            board.deselect()
            board.state = Unlocked_State()
            return

        row, col = cell_index
        square = board.get_square(row, col)

        if cell_index == board.selected_square_pos:
            return

        if not board.is_empty_square(row, col):
            board.select_square(row, col)
        elif square.state == SquareState.SELECTABLE:
            board.move_selected_to(row, col)
            board.deselect()
            board.state = Unlocked_State()
        # If you click an empty, unselectable square. Nothing happens (maybe you misclicked)








