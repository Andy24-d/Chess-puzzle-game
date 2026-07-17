# Example file showing a circle moving on screen
import pygame
from typing import Final
from board import Board
from square import Square, SquareState

#Constants
FPS_limit: Final = 60

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
board = Board(screen)
board.grid[0][0].state = SquareState.HIGHLIGHTED
board.grid[2][1].set_state(SquareState.SELECTABLE)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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