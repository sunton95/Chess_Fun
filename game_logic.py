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
import board
from postition import *
from pieces.king import *
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
def check_for_check(self, square_to_ceck, color):
    avilable_moves = []
    
    for piece in self.game_state:
        if(piece.color != color):
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
        check = check_for_check(self, new_pos, selected_piece.color)
        casteling_check(self)
    else:
        check = check_for_check(self, king_position, selected_piece.color)

    move_while_check(self, new_pos, king_position, selected_piece)

    #Shifts so each player take one turn each. White begins
    #move_order(self, new_pos, selected_piece)
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
        check = check_for_check(self, new_pos, selected_piece.color)
    else:
        check = check_for_check(self, king_position, selected_piece.color)

    if(check == True):
        self.game_state.clear()
        self.board_setup(old_state)
        board.mark_king()
    
    return None

def casteling_check(self):
    king_side_check_white = False
    queen_side_check_white = False
    king_side_check_black = False
    queen_side_check_black = False
    
    if(check_for_check(self, Position(7, 1), "White")):
        king_side_check_white = True
    if(check_for_check(self, Position(6, 1), "White")):
        king_side_check_white = True
    if(check_for_check(self, Position(5, 1), "White")):
        king_side_check_white = True

    if(king_side_check_white == True):
        self.flags.king_side_check_white = True
    else:
        self.flags.king_side_check_white = False

    if(check_for_check(self, Position(5, 1), "White")):
        queen_side_check_white = True
    if(check_for_check(self, Position(4, 1), "White")):
        queen_side_check_white = True
    if(check_for_check(self, Position(3, 1), "White")):
        queen_side_check_white = True
    if(check_for_check(self, Position(2, 1), "White")):
        queen_side_check_white = True

    if(queen_side_check_white == True):
        self.flags.queen_side_check_white = True
    else:
        self.flags.queen_side_check_white = False

    if(check_for_check(self, Position(5, 8), "Black")):
        king_side_check_black = True
    if(check_for_check(self, Position(6, 8), "Black")):
        king_side_check_black = True
    if(check_for_check(self, Position(7, 8), "Black")):
        king_side_check_black = True


    if(king_side_check_black == True):
        self.flags.king_side_check_black = True
    else:
        self.flags.king_side_check_black = False

    if(check_for_check(self, Position(5, 8), "Black")):
        queen_side_check_black = True
    if(check_for_check(self, Position(4, 8), "Black")):
        queen_side_check_black = True
    if(check_for_check(self, Position(3, 8), "Black")):
        queen_side_check_black = True
    if(check_for_check(self, Position(2, 8), "Black")):
        queen_side_check_black = True

    if(queen_side_check_black == True):
        self.flags.queen_side_check_black = True
    else:
        self.flags.queen_side_check_black = False

    


    
