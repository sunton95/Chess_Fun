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
import time
from pieces.pieces_main import *
# =============================================================================
# Current best 2262.64 Nodes per sec
# Test is rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
# With 4 nodes

screen = None
#resolution of the game
#pygame.init()
#screen = pygame.display.set_mode((800, 800))
#pygame.display.set_caption('Extreme Chess')

#variables for draging the pices in UI
selected_piece = None
drop_pos = None

#A string on how the board will be set up for play 
FEN_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

#Initilize the game and pieces posisiton
board_state = GameBoard(move_number = 0)
#board_state.init_images()
board_state.board_setup(FEN_string)
casteling_check(board_state)

for piece in board_state.game_state:
   if(piece.label == "K"):
      selected_piece = piece
      #BaseLine Elapsed time = 9.9493 knight
      #BaseLine Elapsed time = 50.7357 king


depth = 4
#ai.chess_engine(board_state, depth, screen)
start = time.time()
for x in range(0, 100000):
   piece.move(None, board_state.game_state, board_state.flags)
end = time.time()

print("Func 1, Elapsed time = {:.4f}".format((end - start)))

start = time.time()
for x in range(0, 1000):
   generate_fen_string(board_state)
end = time.time()

print("Func 2, Elapsed time = {:.4f}".format((end - start)))

#nodes = ai.scuffedfish.nodes
#print("Done, Nodes = {}, Elapsed time = {:.4f}, Nodes per second = {:.2f}, Pieces Captured = {}".format(nodes, (end - start), (nodes/(end - start)), Pieces.captures))

def kek():
   pygame.display.update()
   pygame.time.delay(33)

   while(1):
      for event in pygame.event.get():
         if event.type in (QUIT, KEYDOWN):
            running = False
            sys.exit()

#kek()