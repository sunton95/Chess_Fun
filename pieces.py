from os import stat
from postition import *

class Pieces:
    def __init__(self, color, position, label):
        self.color = color
        self.position = Position(position[0], position[1])
        self.label = label

    def __str__(self):
        return "{} {}".format(self.color, self.position)


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
        
        for pieces in list:
            if pieces.position == Position((self.position.x + 1), (self.position.y + 1)) and pieces.color != self.color:
                available_moves.append(Position((self.position.x + 1), (self.position.y + 1)))
            elif pieces.position == Position((self.position.x - 1), (self.position.y + 1)) and pieces.color != self.color:
                available_moves.append(Position((self.position.x - 1), (self.position.y + 1)))

            for move in available_moves:
                if move == pieces.position and self.color == pieces.color:
                    available_moves.remove(move)
                elif pieces.position == Position(self.position.x, (self.position.y + 1)):
                    available_moves.remove(Position(self.position.x, (self.position.y + 1)))

        self.pawn_take(cord, list, available_moves)

    def pawn_move_black(self, cord, list):
        available_moves = []
        available_moves.append(Position(self.position.x, (self.position.y - 1)))

        if self.position.y == 7:
            available_moves.append(Position(self.position.x, (self.position.y - 2)))

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

        self.pawn_take(cord, list, available_moves)

    def pawn_take(self, cord, list, available_moves):
        for move in available_moves:
            if move == cord:
                for pieces in list:
                    if pieces.position == move:
                        list.remove(pieces)
                self.position = cord
                break


class Rook(Pieces):
    def move(self, cord, list):
        available_moves = []
        self.position = cord

class Bishop(Pieces):
    def move(self, cord, list):
        available_moves = []
        self.position = cord

class Knight(Pieces):
    def move(self, cord, list):
        available_moves = []
        self.position = cord

class King(Pieces):
    def move(self, cord, list):
        available_moves = []
        self.position = cord

class Queen(Pieces):
    def move(self, cord, list):
        available_moves = []
        self.position = cord