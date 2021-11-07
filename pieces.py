from postition import *

class Pieces:
    def __init__(self, color, position, label):
        self.color = color
        self.position = Position(position[0], position[1])
        self.label = label


    def __str__(self):
        return "{} {}".format(self.color, self.position)


class Pawn(Pieces):
    pass

class Rook(Pieces):
    pass

class Bishop(Pieces):
    pass

class Knight(Pieces):
    pass

class King(Pieces):
    pass

class Queen(Pieces):
    pass