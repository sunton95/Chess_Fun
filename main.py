# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-03-17
# =============================================================================
""""""
# =============================================================================
# TODO
#
# =============================================================================
# Imports
from board import *
from postition import *
import sys, pygame
from pygame.locals import *
# =============================================================================

pygame.init()

#A string on how the board will be set up for play
FEN_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

#resolution of the game
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Extreme Chess')

#Initilize the game and pieces posisiton
b1 = GameBoard(move_number = 0)
images = b1.init_images()
b1.board_setup(FEN_string, images)

#variables for draging the pices in UI
selected_piece = None
drop_pos = None

while(1):
    piece = get_square_under_mouse(b1.game_state)
    print(b1.move_number)

    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            running = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if piece != None:
                selected_piece = piece
        elif event.type == pygame.MOUSEBUTTONUP:
            if drop_pos != None and selected_piece != None:
                b1.move_piece(drop_pos, selected_piece)
            selected_piece = None
            drop_pos = None

    draw_background(screen)
    drop_pos = draw_drag(screen, selected_piece, b1.game_state)
    b1.draw_pieces(screen, selected_piece)

    pygame.display.update()
    pygame.time.delay(33)
