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
    def move(self, cord, list):
        available_moves = []
        available_moves.append(Position((self.position.x + 1), (self.position.y + 2)))
        available_moves.append(Position((self.position.x + 2), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y + 2)))
        available_moves.append(Position((self.position.x - 2), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y - 2)))
        available_moves.append(Position((self.position.x - 2), (self.position.y - 1)))
        available_moves.append(Position((self.position.x + 1), (self.position.y - 2)))
        available_moves.append(Position((self.position.x + 2), (self.position.y - 1)))

        self.find_freindly(list, available_moves)
        self.piece_take(cord, list, available_moves)
        return available_moves