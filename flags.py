class Flags:
    def __init__(self, 
                white_queen_side_castling,
                white_king_side_castling,
                black_king_side_castling,
                black_queen_side_castling):

        self.white_queen_side_castling = white_queen_side_castling
        self.white_king_side_castling = white_king_side_castling
        self.black_king_side_castling = black_king_side_castling
        self.black_queen_side_castling = black_queen_side_castling

class En_passant:
    def __init__(self, target, move_number):
        self.target = target
        self.move_number = move_number