# Board's Cells. Cells store a single piece each.

class Cell:
    def __init__(self, row, col, rect):
        self.row = row
        self.col = col
        self.rect = rect
        self.piece = None

    def put_piece(self, piece):
        self.piece = piece