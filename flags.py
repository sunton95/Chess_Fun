class Flags:
    def __init__(self, 
                white_queen_side_castling,
                white_king_side_castling,
                black_king_side_castling,
                black_queen_side_castling,
                en_passant_target):

        self.white_queen_side_castling = white_queen_side_castling
        self.white_king_side_castling = white_king_side_castling
        self.black_king_side_castling = black_king_side_castling
        self.black_queen_side_castling = black_queen_side_castling
        self.en_passant_target = en_passant_target