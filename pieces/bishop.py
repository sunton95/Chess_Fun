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

class Bishop(Pieces):
    def move(self, cord, list):
        available_moves = []
        pieces_on_same_lane = list
        move_dir = (Position(1, 1),
                    Position(1, -1),
                    Position(-1, 1),
                    Position(-1, -1))


        available_moves = self.QRB_move(available_moves, pieces_on_same_lane, move_dir)
        self.piece_take(cord, list, available_moves)
        return available_moves