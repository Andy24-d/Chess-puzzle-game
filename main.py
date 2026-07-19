# Example file showing a circle moving on screen
import pygame
from typing import Final
from board import Board
from square import Square, SquareState
from game_pieces import Knight, Queen, Bishop, Rook, King

#Constants
FPS_limit: Final = 60

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
board = Board(screen)
knight_test = Knight()
board.add_piece(knight_test, 2, 0)
queen_test = Queen()
board.add_piece(queen_test, 1, 1)
bishop_test = Bishop()
board.add_piece(bishop_test, 0, 2)
rook_test = Rook()
board.add_piece(rook_test, 0, 0)
king_test = King()
board.add_piece(king_test, 2, 1)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 1 means left click
            if event.button == 1:
                board.handle_click(event.pos)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill( (239, 227, 175) )


    board.draw()



    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS_limit) / 1000

pygame.quit()