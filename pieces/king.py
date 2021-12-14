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

class King(Pieces):

    image_white = None
    image_black = None

    def __init__(self, color, position, label):
        super().__init__(color, position, label)
        if(self.color == "White"):
            self.image = King.image_white
        else:
            self.image = King.image_black
    
    def move(self, cord, list):
        available_moves = []
        available_moves.append(Position((self.position.x + 1), (self.position.y)))
        available_moves.append(Position((self.position.x + 1), (self.position.y + 1)))
        available_moves.append(Position((self.position.x + 1), (self.position.y - 1)))
        available_moves.append(Position((self.position.x), (self.position.y - 1)))
        available_moves.append(Position((self.position.x), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y)))
        available_moves.append(Position((self.position.x - 1), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y - 1)))

        self.find_freindly(list, available_moves)
        self.piece_take(cord, list, available_moves)
        return available_moves