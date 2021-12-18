# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-18
""""""
# =============================================================================
# TODO
# =============================================================================
# Imports
import random

from pygame import init
# =============================================================================
class scuffedfish:
    def __init__(self, piece_position, possible_move):
        self.piece_position = piece_position
        self.possible_move = possible_move


def random_move(self):
    avilable_moves = []

    for piece in self.game_state:
        if(piece.color == "Black"):
            moves = piece.move(None, self.game_state, self.flags)
            for move in moves:
                if(move.x >= 1 and move.x <= 8):
                    if(move.y >= 1 and move.y <= 8):
                        avilable_moves.append(scuffedfish(piece.position, move))


    move_range = len(avilable_moves)
    x = random.randint(0, move_range)

    for piece in self.game_state:
        if(piece.position == avilable_moves[x].piece_position):
            piece.move(avilable_moves[x].possible_move, self.game_state, self.flags)
        
    self.move_number += 1

    avilable_moves = None
    




