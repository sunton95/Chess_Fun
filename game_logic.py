# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-13
""""""
# =============================================================================
# TODO
#Bugg when i move the piece to a squre that is not valid but another square the move_number goes up
# =============================================================================
# Imports
import pygame
from pieces.pawn import Pawn
from postition import *
import board
import pieces.king as king
# =============================================================================
def find_king(self, color):
    for piece in self.game_state:
        if(color == "White"):
            if(piece.label == 'K'):
                return piece.position
        elif(color == "Black"):
            if(piece.label == 'k'):
                return piece.position

#Returns True if the square in question is in check otherwise false
def check_for_check(self, square_to_ceck):
    avilable_moves = []
    
    for piece in self.game_state:
        moves = piece.move(None, self.game_state, self.flags)
        for move in moves:
                if(move.x >= 1 and move.x <= 8):
                    if(move.y >= 1 and move.y <= 8):
                        avilable_moves.append(move)

    for move in avilable_moves:
        if(move == square_to_ceck):
            return True

    return False


#Gets a piece on the board
def get_square_under_mouse(game_state):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x = int((mouse_pos[0] // 100) + 1)
    y = int(7 - (mouse_pos[1] // 100) + 1)
    for piece in game_state:
        if piece.position == Position(x, y):
            return piece
    return None

 #Position input
def move_piece(self, new_pos, selected_piece):
    index = 0

    #If the piece dont move cancel the action
    if selected_piece.position == new_pos:
        return None

    #TODO add a function that makes sure the move does not generate a check on self
    king_position = find_king(self, selected_piece.color)

    if(selected_piece.label == 'K' or selected_piece.label == 'k'):
        check = check_for_check(self, new_pos)
        king.casteling_check(self)
    else:
        check = check_for_check(self, king_position)

    if(check == True):
        board.mark_king()
        move_while_check(self, new_pos, king_position, selected_piece)
        return None

    #Shifts so each player take one turn each. White begins
    move_order(self, new_pos, selected_piece)
    #move_no_order_testing(self, new_pos, selected_piece)
    
def move_order(self, new_pos, selected_piece):
    if ((self.move_number) % 2) == 0:
        if (selected_piece.color == "Black"):
            selected_piece.move(new_pos, self.game_state, self.flags) 
            self.move_number += 1
    elif((self.move_number) % 2) == 1:
        if (selected_piece.color == "White"):
            selected_piece.move(new_pos, self.game_state, self.flags) 
            self.move_number += 1

def move_no_order_testing(self, new_pos, selected_piece):
    selected_piece.move(new_pos, self.game_state, self.flags) 
    self.move_number += 1

def move_while_check(self, new_pos, king_position, selected_piece):
    old_state = board.generate_fen_string(self)
    move_order(self, new_pos, selected_piece)

    if(selected_piece.label == 'K' or selected_piece.label == 'k'):
        check = check_for_check(self, new_pos)
    else:
        check = check_for_check(self, king_position)

    if(check == True):
        self.game_state.clear()
        self.board_setup(old_state)
    
    return None

    


    
