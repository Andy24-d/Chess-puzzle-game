# Example file showing a circle moving on screen
import pygame
from typing import Final
from board import Board
from square import Square, SquareState
from game_pieces import Knight, Queen, Bishop, Rook, King
from UI_buttons import Button, act_reset, act_undo, act_do, act_flip


#Constants
FPS_limit: Final = 60
objective_dark  = (76, 53, 24)
objective_light = (172, 135, 86)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Board initial setups
board = Board(screen)
board.setup()
objective_board = Board(screen, 300, 820, 340, dark_sq=objective_dark, light_sq=objective_light)
objective_board.border_thickness = 4
objective_board.setup_solvable(board)
objective_board.lock()

#Buttons setup
font_btn = pygame.font.SysFont(None, 46)

buttons = [
    Button((735, 120, 200, 60), "New Game", on_click=lambda: act_reset(board, objective_board), font=font_btn),
    Button((935, 120, 130, 60), "Undo", act_undo, font=font_btn),
    Button((1065, 120, 100, 60), "Do", act_do, font=font_btn),

    # fila de abajo
    Button((735, 210, 80, 60), "↶", lambda: board.rotate_inverse(), font=font_btn),
    Button((815, 210, 80, 60), "↷", lambda: board.rotate_clock(), font=font_btn),
    Button((895, 210, 160, 60), "Flip H", lambda: board.flip_horizontal(), font=font_btn),
    Button((1055, 210, 160, 60), "Flip V", lambda: board.flip_vertical(), font=font_btn),
]

BG = (239, 227, 175)





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
            if event.button == 2:
                board.deselect()
                board.setup()
                objective_board.setup_solvable(board)

        for b in buttons:
            b.handle_event(event)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill( BG )

    board.draw()
    objective_board.draw()

    for b in buttons:
        b.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(FPS_limit) / 1000

pygame.quit()