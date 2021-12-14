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

    def move(self, cord, board_state, flags):
        available_moves = []
        move_dir = (Position(1, 0),
                    Position(0, 1),
                    Position(-1, 0),
                    Position(0, -1))


        #If the rook moves castling ability is removed
        if(cord != None):
            if(self.position == Position(1, 1)):
                flags.white_queen_side_castling = False
            elif(self.position== Position(8, 1)):
                flags.white_king_side_castling = False
            elif(self.position == Position(1, 8)):
                flags.black_queen_side_castling = False
            elif(self.position == Position(8, 8)):
                flags.black_king_side_castling = False

        available_moves = self.QRB_move(available_moves, board_state, move_dir)
        self.piece_take(cord, board_state, available_moves, flags) 
        return available_moves