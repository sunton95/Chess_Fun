from board import *
from postition import *


FEN_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

b1 = GameBoard()

b1.board_setup(FEN_string)

print(Position.chess_notation_to_cord("A1"))
print(Position.chess_notation_to_cord("A2"))
print(Position.chess_notation_to_cord("A3"))
print(Position.chess_notation_to_cord("B2"))
print(Position.chess_notation_to_cord("H2"))

# while(1):
#     b1.draw_board()
#     move = input("Input a move:")