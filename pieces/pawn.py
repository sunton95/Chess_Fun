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

    def move(self, cord, list):
        if self.color == "White":
            return self.pawn_move_white(cord, list)
        elif self.color == "Black":
            return self.pawn_move_black(cord, list)

    def pawn_move_white(self, cord, list):
        available_moves = []
        available_moves.append(Position(self.position.x, (self.position.y + 1)))

        if self.position.y == 2:
            available_moves.append(Position(self.position.x, (self.position.y + 2)))
        
        #Looking for if there are pieces in places that white can take
        for pieces in list:
            if pieces.position == Position((self.position.x + 1), (self.position.y + 1)) and pieces.color != self.color:
                available_moves.append(Position((self.position.x + 1), (self.position.y + 1)))
            elif pieces.position == Position((self.position.x - 1), (self.position.y + 1)) and pieces.color != self.color:
                available_moves.append(Position((self.position.x - 1), (self.position.y + 1)))

            for move in available_moves:
                if pieces.position == Position(self.position.x, (self.position.y + 1)):
                    available_moves.remove(Position(self.position.x, (self.position.y + 1)))
                elif move == pieces.position and self.color == pieces.color:
                    available_moves.remove(move)

        self.piece_take(cord, list, available_moves)
        return available_moves
    
    def pawn_move_black(self, cord, list):
        available_moves = []
        available_moves.append(Position(self.position.x, (self.position.y - 1)))

        if self.position.y == 7:
            available_moves.append(Position(self.position.x, (self.position.y - 2)))

        #Looking for if there are pieces in places that black can take
        for pieces in list:
            if pieces.position == Position((self.position.x - 1), (self.position.y - 1)) and pieces.color != self.color:
                available_moves.append(Position((self.position.x - 1), (self.position.y - 1)))
            elif pieces.position == Position((self.position.x + 1), (self.position.y - 1)) and pieces.color != self.color:
                available_moves.append(Position((self.position.x + 1), (self.position.y - 1)))
            
            for move in available_moves:
                if move == pieces.position and self.color == pieces.color:
                    available_moves.remove(move)
                elif pieces.position == Position(self.position.x, (self.position.y - 1)):
                    available_moves.remove(Position(self.position.x, (self.position.y - 1)))

        self.piece_take(cord, list, available_moves)
        return available_moves
