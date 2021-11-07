from board import *


FEN_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

b1 = GameBoard()

b1.board_setup(FEN_string)


while(1):
    b1.draw_board()
    username = input("Input a move:")