from os import stat
from postition import *

class Pieces:
    def __init__(self, color, position, label):
        self.color = color
        self.position = Position(position[0], position[1])
        self.label = label

    def __str__(self):
        return "{} {}".format(self.color, self.position)
    
    def find_freindly(self, list, available_moves):
        for pieces in list:
            for move in available_moves:
                if move == pieces.position and self.color == pieces.color:
                    available_moves.remove(move)

    def piece_take(self, cord, list, available_moves):
        for move in available_moves:
            if move == cord:
                for pieces in list:
                    if pieces.position == move:
                        list.remove(pieces)
                self.position = cord
                break
    
    def QRB_move(self, available_moves, pieces_on_same_lane, move_dir):
        for dir in move_dir:
            for scalar in range(1, 9):
                check_if_valid = dir.dir_scale(scalar, self.position)

                if(check_if_valid.x > 8 or check_if_valid.y > 8 or check_if_valid.x < 1 or check_if_valid.y < 1):
                    break
                flag = self.check_occupied(available_moves, pieces_on_same_lane, check_if_valid)

                if(flag == True):
                    available_moves.append(check_if_valid)
                else:
                    break

        return available_moves

    def check_occupied(self, available_moves, pieces_on_same_lane, check_if_valid):
        for piece in pieces_on_same_lane:
            if piece.position == check_if_valid:
                if piece.color == self.color:
                    return False
                if piece.color != self.color:
                    available_moves.append(check_if_valid)
                    return False
        return True
        

class Pawn(Pieces):

    def move(self, cord, list):
        if self.color == "White":
            self.pawn_move_white(cord, list)
        elif self.color == "Black":
            self.pawn_move_black(cord, list)

    def pawn_move_white(self, cord, list):
        available_moves = []
        available_moves.append(Position(self.position.x, (self.position.y + 1)))

        if self.position.y == 2:
            available_moves.append(Position(self.position.x, (self.position.y + 2)))
        
        #Looking for if there are pieces in places that white can take
        for pieces in list:
            if pieces.position == Position((self.position.x + 1), (self.position.y + 1)) and pieces.color != self.color:
                available_moves.append(Position((self.position.x + 1), (self.position.y + 1)))
            elif pieces.position == Position((self.position.x - 1), (self.position.y + 1)) and pieces.color != self.color:
                available_moves.append(Position((self.position.x - 1), (self.position.y + 1)))

            for move in available_moves:
                if pieces.position == Position(self.position.x, (self.position.y + 1)):
                    available_moves.remove(Position(self.position.x, (self.position.y + 1)))
                    available_moves.remove(Position(self.position.x, (self.position.y + 2)))
                elif move == pieces.position and self.color == pieces.color:
                    available_moves.remove(move)

                

        self.piece_take(cord, list, available_moves)

    def pawn_move_black(self, cord, list):
        available_moves = []
        available_moves.append(Position(self.position.x, (self.position.y - 1)))

        if self.position.y == 7:
            available_moves.append(Position(self.position.x, (self.position.y - 2)))

        #Looking for if there are pieces in places that black can take
        for pieces in list:
            if pieces.position == Position((self.position.x - 1), (self.position.y - 1)) and pieces.color != self.color:
                available_moves.append(Position((self.position.x - 1), (self.position.y - 1)))
            elif pieces.position == Position((self.position.x + 1), (self.position.y - 1)) and pieces.color != self.color:
                available_moves.append(Position((self.position.x + 1), (self.position.y - 1)))
            
            for move in available_moves:
                if move == pieces.position and self.color == pieces.color:
                    available_moves.remove(move)
                elif pieces.position == Position(self.position.x, (self.position.y - 1)):
                    available_moves.remove(Position(self.position.x, (self.position.y - 1)))

        self.piece_take(cord, list, available_moves)

class Rook(Pieces):
    def move(self, cord, list):
        available_moves = []
        pieces_on_same_lane = list
        move_dir = (Position(1, 0),
                    Position(0, 1),
                    Position(-1, 0),
                    Position(0, -1))

        available_moves = self.QRB_move(available_moves, pieces_on_same_lane, move_dir)
        self.piece_take(cord, list, available_moves) 
    
class Bishop(Pieces):
    def move(self, cord, list):
        available_moves = []
        pieces_on_same_lane = list
        move_dir = (Position(1, 1),
                    Position(1, -1),
                    Position(-1, 1),
                    Position(-1, -1))


        available_moves = self.QRB_move(available_moves, pieces_on_same_lane, move_dir)
        self.piece_take(cord, list, available_moves)

class Knight(Pieces):
    def move(self, cord, list):
        available_moves = []
        available_moves.append(Position((self.position.x + 1), (self.position.y + 2)))
        available_moves.append(Position((self.position.x + 2), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y + 2)))
        available_moves.append(Position((self.position.x - 2), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y - 2)))
        available_moves.append(Position((self.position.x - 2), (self.position.y - 1)))
        available_moves.append(Position((self.position.x + 1), (self.position.y - 2)))
        available_moves.append(Position((self.position.x + 2), (self.position.y - 1)))

        self.find_freindly(list, available_moves)
        self.piece_take(cord, list, available_moves)

class King(Pieces):
    def move(self, cord, list):
        available_moves = []
        available_moves.append(Position((self.position.x + 1), (self.position.y)))
        available_moves.append(Position((self.position.x + 1), (self.position.y + 1)))
        available_moves.append(Position((self.position.x + 1), (self.position.y - 1)))
        available_moves.append(Position((self.position.x), (self.position.y - 1)))
        available_moves.append(Position((self.position.x), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y)))
        available_moves.append(Position((self.position.x - 1), (self.position.y + 1)))
        available_moves.append(Position((self.position.x - 1), (self.position.y - 1)))

        self.find_freindly(list, available_moves)
        self.piece_take(cord, list, available_moves)

class Queen(Pieces):
        def move(self, cord, list):
            available_moves = []
            pieces_on_same_lane = list
            move_dir = (Position(1, 1),
                        Position(1, -1),
                        Position(-1, 1),
                        Position(-1, -1),
                        Position(1, 0),
                        Position(0, 1),
                        Position(-1, 0),
                        Position(0, -1))

            available_moves = self.QRB_move(available_moves, pieces_on_same_lane, move_dir)
            self.piece_take(cord, list, available_moves)


if __name__ == "__main__":
    import main