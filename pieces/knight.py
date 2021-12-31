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

class Knight(Pieces):

    image_white = None
    image_black = None

    def __init__(self, color, position, label):
        super().__init__(color, position, label)
        if(self.color == "White"):
            self.image = Knight.image_white
        else:
            self.image = Knight.image_black

    def move(self, cord, board_state, flags):
        available_moves = []

        available_moves.append(Position((self.position.x + 1), (self.position.y + 2)))
        available_moves.append(Position((self.position.x + 2), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y + 2)))
        available_moves.append(Position((self.position.x - 2), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y - 2)))
        available_moves.append(Position((self.position.x - 2), (self.position.y - 1)))
        available_moves.append(Position((self.position.x + 1), (self.position.y - 2)))
        available_moves.append(Position((self.position.x + 2), (self.position.y - 1)))

        for pieces in board_state:
            for move in available_moves:
                if move == pieces.position and self.color == pieces.color:
                    available_moves.remove(move)

        self.piece_take(cord, board_state, available_moves, flags)

        return available_moves