# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-18
""""""
# =============================================================================
# TODO
# ossible that checkmate fuck this up
# En passant not generated correctly in FEN string
# Have a varible that always points to the king, removes some for loops prob
# =============================================================================
# Imports
import random
import board
from pieces.king import King
import game_logic as gl
from pygame import init
from pieces.pawn import Pawn
from postition import Position
import sys, pygame
from pygame.locals import *
# =============================================================================
class scuffedfish:

    nodes = 0
    KNIGHT = 500
    KING = 1000
    QUEEN = 800
    BISHOP = 500
    ROOK = 600
    PAWN = 100

    
    def __init__(self, piece_position, move, eval_score):
        self.piece_position = piece_position
        self.move = move
        self.eval_score = eval_score 

    def __str__(self):
        return "piece = ({}, {}) move = ({}, {})".format(self.piece_position.x,
                                            self.piece_position.y,
                                            self.move.x,
                                            self.move.y )

def fast_check(self, square_to_ceck, attacking_moves):   
    for move in attacking_moves:
        if(move.move.x >= 1 and move.move.x <= 8):
            if(move.move.y >= 1 and move.move.y <= 8):
                if(move.move == square_to_ceck):
                    return True

    return False

def find_nodes_of_pos(self, nodes, depth, color, screen):
    depth = depth - 1
    old_state = board.generate_fen_string(self)
    self.game_state.clear()
    self.board_setup(old_state)

    color, avilable_moves = generate_moves(self, color, old_state)

    if(len(avilable_moves) == 0):     
        print("CheckMate" + " " + old_state)
    
    Pawn.en_passant_target.target = Position(0, 0)
    scuffedfish.nodes += len(avilable_moves)

    if(depth > 0):
        for move in avilable_moves:
            for piece in self.game_state:
                if(piece.position == move.piece_position):
                    self.move_number += 1
                    piece.move(move.move, self.game_state, self.flags)
                    #draw_screen(self, screen)
                    find_nodes_of_pos(self, nodes, depth, color, screen) 

                    self.game_state.clear()
                    self.board_setup(old_state)

def generate_moves(self, color, old_state):
    avilable_moves = []
    attacking_moves = []
    remove_these_moves = []
    
    for piece in self.game_state:
        if(piece.color == color):
            moves = piece.move(None, self.game_state, self.flags)
            for move in moves:
                if(move.x >= 1 and move.x <= 8):
                    if(move.y >= 1 and move.y <= 8):
                        avilable_moves.append(scuffedfish(piece.position, move, None))
        if(piece.color != color):
            moves = piece.move(None, self.game_state, self.flags)
            for move in moves:
                if(move.x >= 1 and move.x <= 8):
                    if(move.y >= 1 and move.y <= 8):
                        attacking_moves.append(scuffedfish(piece.position, move, None))                      
        if(piece.label == 'k'):
            King.black_king_position = piece.position
        if(piece.label == 'K'):
           King.white_king_position = piece.position

    if(color == "White"):
        color = "Black"
        king_position = King.white_king_position
    else:
        color = "White" 
        king_position = King.black_king_position   

    for x, piece in enumerate(self.game_state):
        for move in avilable_moves:
            if(move.piece_position == piece.position):
                self.game_state[x].move(move.move, self.game_state, self.flags) 

                if(piece.label == 'K' or piece.label == 'k'):
                    check = fast_check(self, move.move, attacking_moves)
                else:
                    check = fast_check(self, king_position, attacking_moves)
                
                if(check == True):
                    remove_these_moves.append(move)
                
                piece.position = move.piece_position
                self.game_state.clear()
                self.board_setup(old_state)

    for move in remove_these_moves:
        avilable_moves.remove(move)

    self.game_state.clear()
    self.board_setup(old_state)

    return color,avilable_moves
    
def draw_screen(self, screen):
    self.draw_background(screen)
    self.draw_pieces(screen, None)                    
    pygame.display.update()
    pygame.time.delay(500)

def evaluate_depth(self, nodes, depth, color, screen):
    depth = depth - 1
    old_state = board.generate_fen_string(self)
    self.game_state.clear()
    self.board_setup(old_state)

    color, avilable_moves = generate_moves(self, color, old_state)

    if(len(avilable_moves) == 0):     
        print("CheckMate" + " " + old_state)
    
    Pawn.en_passant_target.target = Position(0, 0)
    scuffedfish.nodes += len(avilable_moves)

    if(depth > 0):
        for move in avilable_moves:
            for piece in self.game_state:
                if(piece.position == move.piece_position):
                    self.move_number += 1
                    piece.move(move.move, self.game_state, self.flags)
                    #draw_screen(self, screen)
                    find_nodes_of_pos(self, nodes, depth, color, screen) 

                    self.game_state.clear()
                    self.board_setup(old_state)


def find_best_move(self, nodes, depth, color, screen):
    old_state = board.generate_fen_string(self)
    self.game_state.clear()
    self.board_setup(old_state)
    possible_moves = []

    color, avilable_moves = generate_moves(self, color, old_state)
    Pawn.en_passant_target.target = Position(0, 0)

    for move in avilable_moves:
        for piece in self.game_state:
            if(piece.position == move.piece_position):
                self.move_number += 1
                pos = piece.position
                piece.move(move.move, self.game_state, self.flags)
                eval_score = evaluate_depth(self, nodes, depth, color, screen)
                possible_moves.append(scuffedfish(pos ,move.move, eval_score))    
                self.game_state.clear()
                self.board_setup(old_state)
                

def chess_engine(self, depth, screen):
    color = ""
    avilable_moves = []
    nodes = 0

    if ((self.move_number) % 2) == 0:
        color = "Black"
    elif((self.move_number) % 2) == 1:
        color = "White"
    
    nodes = find_nodes_of_pos(self, nodes, depth, color, screen)

    #best_move = find_best_move(self, nodes, depth, color, screen)
    
    return nodes
