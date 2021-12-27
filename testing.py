# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-03-17
# =============================================================================
""""""
# =============================================================================
# TODO
# move into check maybe a problem
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

FEN_string = '8/8/8/2k5/2pP4/8/B7/4K3 b - d3 0 3'

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


piece = get_square_under_mouse(board_state.game_state)

casteling_check(board_state)

board_state.draw_background(screen)
board_state.draw_pieces(screen, selected_piece)
depth = 2
ai.chess_engine(board_state, depth, screen)

pygame.display.update()
pygame.time.delay(33)

while(1):
   for event in pygame.event.get():
      if event.type in (QUIT, KEYDOWN):
         running = False
         sys.exit()




[
   {
      "depth":3,
      "nodes":62379,
      "fen":"rnbq1k1r/pp1Pbppp/2p5/8/2B5/8/PPP1NnPP/RNBQK2R w KQ - 1 8"
   },
   {
      "depth":3,
      "nodes":89890,
      "fen":"r4rk1/1pp1qppp/p1np1n2/2b1p1B1/2B1P1b1/P1NP1N2/1PP1QPPP/R4RK1 w - - 0 10"
   },
   {
      "depth":6,
      "nodes":1134888,
      "fen":"3k4/3p4/8/K1P4r/8/8/8/8 b - - 0 1"
   },
   {
      "depth":6,
      "nodes":1015133,
      "fen":"8/8/4k3/8/2p5/8/B2P2K1/8 w - - 0 1"
   },
   {
      "depth":6,
      "nodes":1440467,
      "fen":"8/8/1k6/2b5/2pP4/8/5K2/8 b - d3 0 1"
   },
   {
      "depth":6,
      "nodes":661072,
      "fen":"5k2/8/8/8/8/8/8/4K2R w K - 0 1"
   },
   {
      "depth":6,
      "nodes":803711,
      "fen":"3k4/8/8/8/8/8/8/R3K3 w Q - 0 1"
   },
   {
      "depth":4,
      "nodes":1274206,
      "fen":"r3k2r/1b4bq/8/8/8/8/7B/R3K2R w KQkq - 0 1"
   },
   {
      "depth":4,
      "nodes":1720476,
      "fen":"r3k2r/8/3Q4/8/8/5q2/8/R3K2R b KQkq - 0 1"
   },
   {
      "depth":6,
      "nodes":3821001,
      "fen":"2K2r2/4P3/8/8/8/8/8/3k4 w - - 0 1"
   },
   {
      "depth":5,
      "nodes":1004658,
      "fen":"8/8/1P2K3/8/2n5/1q6/8/5k2 b - - 0 1"
   },
   {
      "depth":6,
      "nodes":217342,
      "fen":"4k3/1P6/8/8/8/8/K7/8 w - - 0 1"
   },
   {
      "depth":6,
      "nodes":92683,
      "fen":"8/P1k5/K7/8/8/8/8/8 w - - 0 1"
   },
   {
      "depth":6,
      "nodes":2217,
      "fen":"K1k5/8/P7/8/8/8/8/8 w - - 0 1"
   },
   {
      "depth":7,
      "nodes":567584,
      "fen":"8/k1P5/8/1K6/8/8/8/8 w - - 0 1"
   },
   {
      "depth":4,
      "nodes":23527,
      "fen":"8/8/2k5/5q2/5n2/8/5K2/8 b - - 0 1"
   }
]