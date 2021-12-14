# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-13
""""""
# =============================================================================
# TODO
#
# =============================================================================
# Imports
from .pieces_main import Pieces
from postition import Position
# =============================================================================

class Rook(Pieces):

    image_white = None
    image_black = None

    def __init__(self, color, position, label):
        super().__init__(color, position, label)
        if(self.color == "White"):
            self.image = Rook.image_white
        else:
            self.image = Rook.image_black

    def move(self, cord, list):
        available_moves = []
        pieces_on_same_lane = list
        move_dir = (Position(1, 0),
                    Position(0, 1),
                    Position(-1, 0),
                    Position(0, -1))

        available_moves = self.QRB_move(available_moves, pieces_on_same_lane, move_dir)
        self.piece_take(cord, list, available_moves) 
        return available_moves