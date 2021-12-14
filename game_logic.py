# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-13
""""""
# =============================================================================
# TODO
#Bugg when i move the pice to a squre that is not valid but another square the move_number goes up
# =============================================================================
# Imports
import pygame
from pieces.pawn import Pawn
from postition import *
# =============================================================================

def check_for_checK(game_state, selected_piece):
    pass

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

    #Add function that looks for check
    check_flag = False
    #check_flag = check_for_check(selected_piece)
    if check_flag == True:
        return None

    #TODO add a function that makes sure the move does not generate a check on self
    
    #Shifts eo each player take one turn each. White begins
    if ((self.move_number) % 2) == 0:
        if (selected_piece.color == "Black"):
            selected_piece.move(new_pos, self.game_state) 
            self.move_number += 1
    elif((self.move_number) % 2) == 1:
        if (selected_piece.color == "White"):
            selected_piece.move(new_pos, self.game_state) 
            self.move_number += 1