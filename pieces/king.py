# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-13
""""""
# =============================================================================
# TODO
# Add so castling is not possible if moving trough a check
# =============================================================================
# Imports
from .pieces_main import Pieces
from postition import Position
import game_logic as gl
# =============================================================================

class King(Pieces):

    image_white = None
    image_black = None

    king_side_check_white = False
    queen_side_check_white = False
    king_side_check_black = False
    queen_side_check_black = False
    

    def __init__(self, color, position, label):
        super().__init__(color, position, label)
        if(self.color == "White"):
            self.image = King.image_white
        else:
            self.image = King.image_black
    
    #Creates a list with the avialable moves at the kings current location. Also checks if casteling is possible
    def move(self, cord, board_state, flags):
        available_moves = []

        #All available moves for the king in normal conditions
        available_moves.append(Position((self.position.x + 1), (self.position.y)))
        available_moves.append(Position((self.position.x + 1), (self.position.y + 1)))
        available_moves.append(Position((self.position.x + 1), (self.position.y - 1)))
        available_moves.append(Position((self.position.x), (self.position.y - 1)))
        available_moves.append(Position((self.position.x), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y)))
        available_moves.append(Position((self.position.x - 1), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y - 1)))

        #Checks if castling is possible and returns the avialbel moves
        self.castling_move(cord, board_state, flags, available_moves)

        #Special move when castling, moves both rook and king
        if(cord == Position(7, 1) and self.position == Position(5, 1)):
            for piece in board_state:
                if(piece.position == Position(8, 1)):
                    piece.position = Position(6, 1)
                    self.position = cord
            return None
        if(cord == Position(3, 1) and self.position == Position(5, 1)):
            for piece in board_state:
                if(piece.position == Position(1, 1)):
                    piece.position = Position(4, 1)
                    self.position = cord
            return None
        if(cord == Position(7, 8) and self.position == Position(5, 8)):
            for piece in board_state:
                if(piece.position == Position(8, 8)):
                    piece.position = Position(6, 8)
                    self.position = cord
            return None
        if(cord == Position(3, 8) and self.position == Position(5, 8)):
            for piece in board_state:
                if(piece.position == Position(1, 8)):
                    piece.position = Position(4, 8)
                    self.position = cord
            return None
        
        #Normal move is made with these functions
        self.find_freindly(board_state, available_moves)
        self.piece_take(cord, board_state, available_moves, flags)
        return available_moves

    #Checks if castling is still possible and generates the move
    def castling_move(self, cord, board_state, flags, available_moves):
        empty_sqaure_king_side = False
        empty_sqaure_queen_side = False

        #Checks that all squares between the king and the rook is empty
        #Castling is not possible if these squares are blocked
        if(self.color == "White"):
            if(flags.white_king_side_castling == True):
                for piece in board_state:
                    if(piece.position == Position(6, 1)):
                        empty_sqaure_king_side = True
                    elif(piece.position == Position(7, 1)):
                        empty_sqaure_king_side = True   
                if(empty_sqaure_king_side == False and King.king_side_check_white == False):
                    available_moves.append(Position(7, 1))

            if(flags.white_queen_side_castling == True):
                for piece in board_state:
                    if(piece.position == Position(4, 1)):
                        empty_sqaure_queen_side = True
                    elif(piece.position == Position(3, 1)):
                        empty_sqaure_queen_side = True
                    elif(piece.position == Position(2, 1)):
                        empty_sqaure_queen_side = True
                if(empty_sqaure_queen_side == False and King.queen_side_check_white == False):
                    available_moves.append(Position(3, 1))

        if(self.color == "Black"):
            if(flags.black_king_side_castling == True):
                for piece in board_state:
                    if(piece.position == Position(6, 8)):
                        empty_sqaure_king_side = True
                    elif(piece.position == Position(7, 8)):
                        empty_sqaure_king_side = True   
                if(empty_sqaure_king_side == False and King.king_side_check_black == False):
                    available_moves.append(Position(7, 8))

            if(flags.black_queen_side_castling == True):
                for piece in board_state:
                    if(piece.position == Position(4, 8)):
                        empty_sqaure_queen_side = True
                    elif(piece.position == Position(3, 8)):
                        empty_sqaure_queen_side = True
                    elif(piece.position == Position(2, 18)):
                        empty_sqaure_queen_side = True
                if(empty_sqaure_queen_side == False and King.queen_side_check_black == False):
                    available_moves.append(Position(3, 8))

        #If the king moves castling ability is removed
        if(cord != None):
            if(self.position == Position(5, 8)):
                flags.black_king_side_castling = False
                flags.black_queen_side_castling = False
            elif(self.position== Position(5, 1)):
                flags.white_king_side_castling = False
                flags.white_queen_side_castling = False

def casteling_check(self):
    king_side_check_white =  gl.check_for_check(self, Position(6, 1))
    king_side_check_white =  gl.check_for_check(self, Position(7, 1))
    king_side_check_white =  gl.check_for_check(self, Position(5, 1))
    if(king_side_check_white == True):
        King.king_side_check_white = True
    else:
        King.king_side_check_white = False

    queen_side_check_white = gl.check_for_check(self, Position(5, 1))
    queen_side_check_white = gl.check_for_check(self, Position(4, 1))
    queen_side_check_white = gl.check_for_check(self, Position(3, 1))
    queen_side_check_white = gl.check_for_check(self, Position(2, 1))
    if(queen_side_check_white == True):
        King.queen_side_check_white = True
    else:
        King.queen_side_check_white = False

    king_side_check_black =  gl.check_for_check(self, Position(5, 8))
    king_side_check_black =  gl.check_for_check(self, Position(6, 8))
    king_side_check_black =  gl.check_for_check(self, Position(7, 8))
    if(king_side_check_black == True):
        King.king_side_check_black = True
    else:
        King.king_side_check_black = False

    queen_side_check_black = gl.check_for_check(self, Position(5, 8))
    queen_side_check_black = gl.check_for_check(self, Position(4, 8))
    queen_side_check_black = gl.check_for_check(self, Position(3, 8))
    queen_side_check_black = gl.check_for_check(self, Position(2, 8))

    if(queen_side_check_black == True):
        King.queen_side_check_black = True
    else:
        King.queen_side_check_black = False

    print(king_side_check_white)
    print(queen_side_check_white)
    print(king_side_check_black)
    print(queen_side_check_black)
