# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-03-17
# =============================================================================
""""""
# =============================================================================
# TODO
# =============================================================================
# Imports
# =============================================================================

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x = {:2}, y =  {:2}".format(self.x, self.y)

    def __add__(self, other):
        return Position((self.x + other.x), (self.y + other.y))

    def convert_coordinates(self):
        return self.x + ((self.y - 1) * 8) - 1

    def __eq__(self, other):
        if (isinstance(other, Position)):
            return self.x == other.x and self.y == other.y

    def dir_scale(self, scalar, org_pos):
        return Position((self.x * scalar + org_pos.x),(self.y * scalar+ org_pos.y))


    @staticmethod
    def chess_notation_to_cord(str):
        array = ["a", "b", "c", "d", "e", "f", "g", "h"]
        x = 1
        
        str = str.lower()

        for i in array:
            if (i == str[0]):
                cord = x
            x += 1

        return Position(cord, int(str[1]))

if __name__ == "__main__":
    import main