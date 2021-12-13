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

class Pawn(Pieces):
    en_passant_target = None

    def move(self, cord, game_state):
        if self.color == "White":
            moves = [Position(0, 1),
                     Position(1, 1),
                     Position(-1, 1),
                    ]
            if(self.position.y == 2):
                moves.append(Position(0,2))

            return self.pawn_move(cord, list, moves)     
        elif self.color == "Black":
            moves = [Position(0, -1),
                     Position(1, -1),
                     Position(-1, -1),
                    ]
            if(self.position.y == 7):
                moves.append(Position(0,-2))

            return self.pawn_move(cord, list, moves)

    def pawn_move(self, cord, list, moves):
        available_moves = []
        
        for move in moves:
            available_moves.append(Position((self.position.x + move.x), (self.position.y + move.y)))

        self.piece_take(cord, list, available_moves)
        return available_moves