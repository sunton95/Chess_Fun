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
from flags import En_passant
from postition import Position
from .queen import Queen
# =============================================================================

class Pawn(Pieces):

    en_passant_target = En_passant(None, None)
    move_number = None
    image_white = None
    image_black = None

    def __init__(self, color, position, label):
        super().__init__(color, position, label)
        if(self.color == "White"):
            self.image = Pawn.image_white
        else:
            self.image = Pawn.image_black

    def move(self, cord, game_state, flags):
        if self.color == "White":
            moves = [Position(0, 1),
                     Position(1, 1),
                     Position(-1, 1),
                    ]
            if(self.position.y == 2):
                moves.append(Position(0,2))

            return self.pawn_move(cord, game_state, moves, flags)     

        elif self.color == "Black":
            moves = [Position(0, -1),
                     Position(1, -1),
                     Position(-1, -1),
                    ]
            if(self.position.y == 7):
                moves.append(Position(0,-2))

            return self.pawn_move(cord, game_state, moves, flags)

    def pawn_move(self, cord, game_state, moves, flags):
        available_moves = []

        #Finds the regulare pawn moves
        self.find_pawn_moves(cord, game_state, moves, available_moves)

        #Generates an en passant move if available first if is for white second for black
        if(Pawn.en_passant_target.target == (moves[1] + self.position)):
            if((Pawn.en_passant_target.move_number + 1) == (Pawn.move_number)):
                available_moves.append(moves[1] + self.position)
        elif(Pawn.en_passant_target.target == (moves[2] + self.position)):
            if((Pawn.en_passant_target.move_number + 1) == (Pawn.move_number)):
                available_moves.append(moves[2] + self.position)

        for move in available_moves:       
            if(move == Pawn.en_passant_target.target and move == cord):
                for piece in game_state:
                    if(piece.position == (cord + Position(0, 1)) or piece.position == (cord + Position(0, -1))):
                        game_state.remove(piece)
                        self.position = cord
                return None
                
        self.piece_take(cord, game_state, available_moves, flags)

        if(cord != None):
            if(cord.y == 8 or cord.y == 1):
                game_state.append(Queen(self.color, (cord.x, cord.y), "Q"))
                game_state.remove(self)
                return None

        return available_moves

    def find_pawn_moves(self, cord, game_state, moves, available_moves):
        available_moves.append(Position((self.position.x + moves[0].x), (self.position.y + moves[0].y)))


        if(len(moves) == 4):
            available_moves.append(Position((self.position.x + moves[3].x), (self.position.y + moves[3].y)))
            if((moves[3] + self.position) == cord):
                if(self.color == "White"):
                    Pawn.en_passant_target = En_passant((cord + Position(0, -1)), Pawn.move_number)
                elif(self.color == "Black"):
                    Pawn.en_passant_target = En_passant((cord + Position(0, 1)), Pawn.move_number)

        for piece in game_state:
            if((moves[0] + self.position) == piece.position):
               available_moves.remove(Position((self.position.x + moves[0].x), (self.position.y + moves[0].y)))
            elif((moves[1] + self.position) == piece.position and piece.color != self.color):
                 available_moves.append(Position((self.position.x + moves[1].x), (self.position.y + moves[1].y)))
            elif((moves[2] + self.position) == piece.position and piece.color != self.color):
                available_moves.append(Position((self.position.x + moves[2].x), (self.position.y + moves[2].y)))
            
            if(len(moves) == 4):
                if((moves[3] + self.position) == piece.position or (moves[0] + self.position) == piece.position):
                    try:
                        available_moves.remove(Position((self.position.x + moves[3].x), (self.position.y + moves[3].y)))
                    except ValueError:
                          print("Kek")