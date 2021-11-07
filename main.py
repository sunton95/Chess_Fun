from board import *
from postition import *


FEN_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

b1 = GameBoard()

b1.board_setup(FEN_string)

while(1):
    b1.draw_board()
    move = input("Input a move:")
    cord1, cord2 = move.split(":")
    b1.move_piece(cord1, cord2)