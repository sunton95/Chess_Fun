# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-03-17
# =============================================================================
""""""
# =============================================================================
# TODO
# Pawn can move trough one puce if two move squaers
# =============================================================================
# Imports
from board import *
from postition import *
import sys, pygame
from pygame.locals import *
from game_logic import *
import ai
# =============================================================================

pygame.init()

#A string on how the board will be set up for play
#FEN_string =  '8/8/8/2k5/2pP4/8/B7/4K3 b - d3 0 3'
#FEN_string =  '8/8/8/8/8/7B/7P/8 w KQ - 3 2'

FEN_string = 'K1k11111/11111111/P1111111/11111111/11111111/11111111/11111111/11111111 w - - 0 1'

#FEN_string =  '8/4k3/8/8/7B/8/8/4KRR2 b KQ - 3 2'
#FEN_string =  '8/4k1bq/8/8/7B/8/8/4K3 b KQ - 3 2'
#FEN_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

#resolution of the game
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Extreme Chess')

#Initilize the game and pieces posisiton
board_state = GameBoard(move_number = 0)
board_state.init_images()
board_state.board_setup(FEN_string)

#variables for draging the pices in UI
selected_piece = None
drop_pos = None

while(1):
    piece = get_square_under_mouse(board_state.game_state)

    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            running = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if piece != None:
                selected_piece = piece
        elif event.type == pygame.MOUSEBUTTONUP:
            if drop_pos != None and selected_piece != None:
                move_piece(board_state, drop_pos, selected_piece)
            selected_piece = None
            drop_pos = None

    casteling_check(board_state)
    
    #if((board_state.move_number) % 2) == 0:
        #ai.random_move(board_state)

    board_state.draw_background(screen)
    drop_pos = board_state.draw_drag(screen, selected_piece, board_state.game_state, board_state.flags)
    board_state.draw_pieces(screen, selected_piece)

    pygame.display.update()
    pygame.time.delay(33)