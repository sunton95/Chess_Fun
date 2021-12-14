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

class Queen(Pieces):

    image_white = None
    image_black = None

    def __init__(self, color, position, label):
        super().__init__(color, position, label)
        if(self.color == "White"):
            self.image = Queen.image_white
        else:
            self.image = Queen.image_black
    
    def move(self, cord, board_state, flags):
        available_moves = []
        move_dir = (Position(1, 1),
                    Position(1, -1),
                    Position(-1, 1),
                    Position(-1, -1),
                    Position(1, 0),
                    Position(0, 1),
                    Position(-1, 0),
                    Position(0, -1))

        available_moves = self.QRB_move(available_moves, board_state, move_dir)
        self.piece_take(cord, board_state, available_moves, flags)
        return available_moves