from os import X_OK


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x = {}, y =  {}".format(self.x, self.y)

    def convert_coordinates(self):
        return self.x + ((self.y - 1) * 8) - 1

    @staticmethod
    def chess_notation_to_cord(str):
        array = ["A", "B", "C", "D", "E", "F", "G", "H"]
        x = 1
        
        for i in array:
            if (i == str[0]):
                cord = x
            x += 1

        return [cord, int(str[1])]

