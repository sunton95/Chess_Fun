from postition import *

class Pieces:
    def __init__(self, color, position):
        self.color = color
        self.position = Position(position[0], position[1])

    def __str__(self):
        return "{} {}".format(self.color, self.position)


class Pawn(Pieces):
    def __init__(self, color, position, label):
        super().__init__(color, position)
        self.label = label

class Rook(Pieces):
    def __init__(self, color, position, label):
        super().__init__(color, position)
        self.label = label

class Bishop(Pieces):
    def __init__(self, color, position, label):
        super().__init__(color, position)
        self.label = label

class Knight(Pieces):
    def __init__(self, color, position, label):
        super().__init__(color, position)
        self.label = label

class King(Pieces):
    def __init__(self, color, position, label):
        super().__init__(color, position)
        self.label = label

class Queen(Pieces):
    def __init__(self, color, position, label):
        super().__init__(color, position)
        self.label = label