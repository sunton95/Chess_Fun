# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-13
""""""
# =============================================================================
# TODO
#
# =============================================================================
# Imports
from .pieces_main import Pieces
from postition import Position
# =============================================================================

class King(Pieces):

    image_white = None
    image_black = None

    def __init__(self, color, position, label):
        super().__init__(color, position, label)
        if(self.color == "White"):
            self.image = King.image_white
        else:
            self.image = King.image_black
    
    def move(self, cord, board_state, flags):
        available_moves = []
        available_moves.append(Position((self.position.x + 1), (self.position.y)))
        available_moves.append(Position((self.position.x + 1), (self.position.y + 1)))
        available_moves.append(Position((self.position.x + 1), (self.position.y - 1)))
        available_moves.append(Position((self.position.x), (self.position.y - 1)))
        available_moves.append(Position((self.position.x), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y)))
        available_moves.append(Position((self.position.x - 1), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y - 1)))

        self.castling_move(cord, board_state, flags, available_moves)

        self.find_freindly(board_state, available_moves)
        self.piece_take(cord, board_state, available_moves, flags)
        return available_moves

    def castling_move(self, cord, board_state, flags, available_moves):
        #If the king moves castling ability is removed
        if(cord != None):
            if(self.position == Position(5, 8)):
                flags.black_king_side_castling = False
                flags.black_queen_side_castling = False
            elif(self.position== Position(5, 1)):
                flags.white_king_side_castling = False
                flags.white_queen_side_castling = False

        empty_sqaure_king_side = False
        empty_sqaure_queen_side = False

        if(self.color == "White"):
            if(flags.white_king_side_castling == True):
                for piece in board_state:
                    if(piece.position == Position(6, 1)):
                        empty_sqaure_king_side = True
                    elif(piece.position == Position(7, 1)):
                        empty_sqaure_king_side = True   
                if(empty_sqaure_king_side == False):
                    available_moves.append(Position(7, 1))

            if(flags.white_queen_side_castling == True):
                for piece in board_state:
                    if(piece.position == Position(4, 1)):
                        empty_sqaure_queen_side = True
                    elif(piece.position == Position(3, 1)):
                        empty_sqaure_queen_side = True
                    elif(piece.position == Position(2, 1)):
                        empty_sqaure_queen_side = True
                if(empty_sqaure_queen_side == False):
                    available_moves.append(Position(3, 1))

        if(self.color == "Black"):
            if(flags.black_king_side_castling == True):
                for piece in board_state:
                    if(piece.position == Position(6, 8)):
                        empty_sqaure_king_side = True
                    elif(piece.position == Position(7, 8)):
                        empty_sqaure_king_side = True   
            if(empty_sqaure_king_side == False):
                available_moves.append(Position(7, 8))

            if(flags.black_queen_side_castling == True):
                for piece in board_state:
                    if(piece.position == Position(4, 8)):
                        empty_sqaure_queen_side = True
                    elif(piece.position == Position(3, 8)):
                        empty_sqaure_queen_side = True
                    elif(piece.position == Position(2, 18)):
                        empty_sqaure_queen_side = True
            if(empty_sqaure_queen_side == False):
                available_moves.append(Position(3, 8))
