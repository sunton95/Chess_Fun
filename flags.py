# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-14
""""""
# =============================================================================
# TODO
#
# =============================================================================
# Imports

# =============================================================================

class Flags:
    def __init__(self, 
                white_queen_side_castling,
                white_king_side_castling,
                black_king_side_castling,
                black_queen_side_castling,
                king_side_check_white,
                queen_side_check_white,
                king_side_check_black,
                queen_side_check_black                
                ):

        self.white_queen_side_castling = white_queen_side_castling
        self.white_king_side_castling = white_king_side_castling
        self.black_king_side_castling = black_king_side_castling
        self.black_queen_side_castling = black_queen_side_castling
        self.king_side_check_white = king_side_check_white
        self.queen_side_check_white = queen_side_check_white
        self.king_side_check_black = king_side_check_black
        self.queen_side_check_black = queen_side_check_black

class En_passant:
    def __init__(self, target, move_number):
        self.target = target
        self.move_number = move_number

    def cord_change(self):
        return 'd3'