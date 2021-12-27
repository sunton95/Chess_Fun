# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-18
""""""
# =============================================================================
# TODO
# =============================================================================
# Imports
import random
import board
from pieces.king import King
import game_logic as gl
from pygame import init
from pieces.pawn import Pawn
from postition import Position
# =============================================================================
class scuffedfish:
    def __init__(self, piece_position, possible_move):
        self.piece_position = piece_position
        self.possible_move = possible_move

    def __str__(self):
        return "piece = ({}, {}) move = ({}, {})".format(self.piece_position.x,
                                            self.piece_position.y,
                                            self.possible_move.x,
                                            self.possible_move.y )

def random_move(self):

    Pawn.move_number = self.move_number

    avilable_moves = generate_moves(self)

    move_range = len(avilable_moves)

    if(move_range == 0):
        print("CHECK m8 motherfuicker")
        return None

    x = random.randint(0, (move_range - 1))

    if(self.move_number == 4):
         self.game_state[0].move(Position(4,6), self.game_state, self.flags)

    for piece in self.game_state:
        if(piece.position == avilable_moves[x].piece_position):
            piece.move(avilable_moves[x].possible_move, self.game_state, self.flags)
        
    self.move_number += 1

    avilable_moves.clear()

#TODO the ai can move into a check position
def remove_invalid_moves(self, avilable_moves, king_position, color):
    old_state = board.generate_fen_string(self)
    remove_these_moves = []
    self.game_state.clear()
    self.board_setup(old_state)

    for x, piece in enumerate(self.game_state):
        for move in avilable_moves:
            if(move.piece_position == piece.position):
                self.game_state[x].move(move.possible_move, self.game_state, self.flags) 

                if(piece.label == 'K' or piece.label == 'k'):
                    check = gl.check_for_check(self, move.possible_move, color)
                else:
                    check = gl.check_for_check(self, king_position, color)
                
                if(check == True):
                    remove_these_moves.append(move)
                
                piece.position = move.piece_position
                self.game_state.clear()
                self.board_setup(old_state)

    for move in remove_these_moves:
        avilable_moves.remove(move)

    self.game_state.clear()
    self.board_setup(old_state)
    return avilable_moves

def generate_moves(self):
    avilable_moves = []

    for piece in self.game_state:
        if(piece.color == "Black"):
            moves = piece.move(None, self.game_state, self.flags)
            for move in moves:
                if(move.x >= 1 and move.x <= 8):
                    if(move.y >= 1 and move.y <= 8):
                        avilable_moves.append(scuffedfish(piece.position, move))
    
    king_position = gl.find_king(self, "Black")
    avilable_moves = remove_invalid_moves(self, avilable_moves, king_position, "Black")

    return avilable_moves

def depth_moves(self, nodes, depth, color):
    depth = depth - 1
    old_state = board.generate_fen_string(self)
    self.game_state.clear()
    self.board_setup(old_state)

    avilable_moves = []

    king_position = gl.find_king(self, color)
    
    for piece in self.game_state:
        if(piece.color == color):
            moves = piece.move(None, self.game_state, self.flags)
            for move in moves:
                if(move.x >= 1 and move.x <= 8):
                    if(move.y >= 1 and move.y <= 8):
                        avilable_moves.append(scuffedfish(piece.position, move))

    avilable_moves = remove_invalid_moves(self, avilable_moves, king_position, color)
    if(color == "White"):
        color = "Black"
    else:
        color = "White"

    for move in avilable_moves:
        if(depth > 0):
            nodes += 1
            for piece in self.game_state:
                if(piece.position == move.piece_position):
                    self.move_number += 1
                    piece.move(move.possible_move, self.game_state, self.flags)
            nodes = depth_moves(self, nodes, depth, color)         
                    
        else:
            nodes += 1

        self.game_state.clear()
        self.board_setup(old_state)
            
    #print("nodes = {}".format(nodes))
    return nodes

def chess_engine(self, depth):
    color = ""
    avilable_moves = []
    nodes = 0

    if ((self.move_number) % 2) == 0:
        color = "Black"
    elif((self.move_number) % 2) == 1:
        color = "White"
    
    nodes = depth_moves(self, nodes, depth, color)
    
    return nodes
