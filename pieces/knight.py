# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-13
""""""
# =============================================================================
# TODO
#
# =============================================================================
# Imports
from pygame.locals import Color
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
        
        move_one = False
        move_two = False
        move_tree = False
        move_four = False
        move_five = False
        move_six = False
        move_seven = False
        move_eight = False

        for piece in board_state:
            if(piece.color == self.color):
                if(piece.position == Position((self.position.x + 1), (self.position.y + 2))):
                    move_one = True
                if(piece.position == Position((self.position.x + 2), (self.position.y + 1))):
                    move_two = True
                if(piece.position == Position((self.position.x - 1), (self.position.y + 2))):
                    move_tree = True
                if(piece.position == Position((self.position.x - 2), (self.position.y + 1))):
                    move_four = True
                if(piece.position == Position((self.position.x - 1), (self.position.y - 2))):
                    move_five = True
                if(piece.position == Position((self.position.x - 2), (self.position.y - 1))):
                    move_six = True
                if(piece.position == Position((self.position.x + 1), (self.position.y - 2))):
                    move_seven = True
                if(piece.position == Position((self.position.x + 2), (self.position.y - 1))):
                    move_eight = True
        
        if(move_one == False):
            available_moves.append(Position((self.position.x + 1), (self.position.y + 2)))
        if(move_two == False):
            available_moves.append(Position((self.position.x + 2), (self.position.y + 1)))
        if(move_tree == False):
            available_moves.append(Position((self.position.x - 1), (self.position.y + 2)))
        if(move_four == False):
            available_moves.append(Position((self.position.x - 2), (self.position.y + 1)))
        if(move_five == False):
            available_moves.append(Position((self.position.x - 1), (self.position.y - 2)))
        if(move_six == False):
            available_moves.append(Position((self.position.x - 2), (self.position.y - 1)))
        if(move_seven == False):
            available_moves.append(Position((self.position.x + 1), (self.position.y - 2)))
        if(move_eight == False):
            available_moves.append(Position((self.position.x + 2), (self.position.y - 1)))


        self.piece_take(cord, board_state, available_moves, flags)

        return available_moves