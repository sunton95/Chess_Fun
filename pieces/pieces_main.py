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

    def piece_take(self, cord, list, available_moves):
        if cord != None:
            for move in available_moves:
                if move == cord:
                    for pieces in list:
                        if pieces.position == move:
                            list.remove(pieces)
                    self.position = cord
                    break
    
    def QRB_move(self, available_moves, pieces_on_same_lane, move_dir):
        for dir in move_dir:
            for scalar in range(1, 9):
                check_if_valid = dir.dir_scale(scalar, self.position)

                if(check_if_valid.x > 8 or check_if_valid.y > 8 or check_if_valid.x < 1 or check_if_valid.y < 1):
                    break
                flag = self.check_occupied(available_moves, pieces_on_same_lane, check_if_valid)

                if(flag == True):
                    available_moves.append(check_if_valid)
                else:
                    break

        return available_moves

    def check_occupied(self, available_moves, pieces_on_same_lane, check_if_valid):
        for piece in pieces_on_same_lane:
            if piece.position == check_if_valid:
                if piece.color == self.color:
                    return False
                if piece.color != self.color:
                    available_moves.append(check_if_valid)
                    return False
        return True    

if __name__ == "__main__":
    import main