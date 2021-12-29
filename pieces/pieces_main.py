# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-13
""""""
# =============================================================================
# TODO
#
# =============================================================================
# Imports
from os import stat
from postition import *
# =============================================================================

#Parent class for all the chesspieces
class Pieces:
    
    captures = 0

    def __init__(self, color, position, label):
        self.color = color
        self.position = Position(position[0], position[1])
        self.label = label

    def __str__(self):
        return "{} {}".format(self.color, self.position)
    
    def find_freindly(self, list, available_moves):
        for pieces in list:
            for move in available_moves:
                if move == pieces.position and self.color == pieces.color:
                    available_moves.remove(move)

    def piece_take(self, cord, list, available_moves, flags):
        if cord != None:
            for move in available_moves:
                if move == cord:
                    for pieces in list:
                        if pieces.position == move:
                            from .rook import Rook
                            if(type(pieces) is Rook):
                                if(pieces.position == Position(1, 1)):
                                    flags.white_queen_side_castling = False
                                elif(pieces.position == Position(8, 1)):
                                    flags.white_king_side_castling = False
                                elif(pieces.position == Position(1, 8)):
                                    flags.black_queen_side_castling = False
                                elif(pieces.position == Position(8, 8)):
                                    flags.black_king_side_castling = False
                            list.remove(pieces)
                            Pieces.captures += 1
                    self.position = cord
                    break
    
    def QRB_move(self, available_moves, board_state, move_dir):
        for dir in move_dir:
            for scalar in range(1, 9):
                check_if_valid = dir.dir_scale(scalar, self.position)

                if(check_if_valid.x > 8 or check_if_valid.y > 8 or check_if_valid.x < 1 or check_if_valid.y < 1):
                    break
                flag = self.check_occupied(available_moves, board_state, check_if_valid)

                if(flag == True):
                    available_moves.append(check_if_valid)
                else:
                    break

        return available_moves

    def check_occupied(self, available_moves, board_state, check_if_valid):
        for piece in board_state:
            if piece.position == check_if_valid:
                if piece.color == self.color:
                    return False
                if piece.color != self.color:
                    available_moves.append(check_if_valid)
                    return False
        return True    

if __name__ == "__main__":
    import main