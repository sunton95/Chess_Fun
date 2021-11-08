from pieces import *
import os

class GameBoard:
    def __init__(self):
        self.game_state = []
        self.position_list = []

    def board_setup(self, FEN_string):
        FEN_string  = FEN_string.split(' ')
        pieces_on_board = FEN_string[0]

        index = [1, 8]

        for x in range(0, 65):
            self.position_list.append(" ")

        for pieces in pieces_on_board:
            if pieces == 'P':
                self.game_state.append(Pawn("White", index, "P")) 
            elif pieces == 'R':
                self.game_state.append(Rook("White", index, "R"))
            elif pieces == 'N':
                self.game_state.append(Knight("White", index, "N"))
            elif pieces == 'B':
                self.game_state.append(Bishop("White", index, "B"))
            elif pieces == 'Q':
                self.game_state.append(Queen("White", index, "Q"))
            elif pieces == 'K':
                self.game_state.append(King("White", index, "K")) 
            elif pieces == 'p':
                self.game_state.append(Pawn("Black", index, "p"))
            elif pieces == 'r':
                self.game_state.append(Rook("Black", index, "r")) 
            elif pieces == 'n':
                self.game_state.append(Knight("Black", index, "n"))         
            elif pieces == 'b':
                self.game_state.append(Bishop("Black", index, "b")) 
            elif pieces == 'q':
                self.game_state.append(Queen("Black", index, "q")) 
            elif pieces == 'k':
                self.game_state.append(King("Black", index, "k"))  
            

            if pieces == "/":
                index[1] -= 1
                index[0] = 1
            elif pieces.isdigit() == True:
                index[0] = int(pieces)
            else:
                index[0] += 1

        #Return True if black to move and false if White move


    def draw_board(self):
        #Clears the terminal before printing a new frame of the game
        os.system('cls||clear')

        #Fills the list with empty placeholders and adds the chess pieces location to the list
        for x in range(0,65):
            self.position_list[x] = " "
        for pieces in self.game_state:
            self.position_list[pieces.position.convert_coordinates()] = pieces.label
            
        print("\033[%d;%dH" % (1, 1))
        for x in range(1,9):
            i = 8 * (x - 1)
            print("|{}|{}|{}|{}|{}|{}|{}|{}|  {}".format(self.position_list[56 - i],
                                                         self.position_list[57 - i],
                                                         self.position_list[58 - i],
                                                         self.position_list[59 - i],
                                                         self.position_list[60 - i],
                                                         self.position_list[61 - i],
                                                         self.position_list[62 - i],
                                                         self.position_list[63 - i],                                                   
                                                         (9 - x)))

        print("")
        print("|{}|{}|{}|{}|{}|{}|{}|{}|".format("A","B","C","D","E","F","G", "H"))
        print("")
    
    def move_piece(self, cord1, cord2):
        org_pos = Position.chess_notation_to_cord(cord1)
        new_pos = Position.chess_notation_to_cord(cord2)
        index = 0

        #Add function that looks for check
        #TODO add a function that makes sure the move does not generate a check on self

        #Finds if there is a piece on the selected square
        for pieces in self.game_state:
            if pieces.position == org_pos:
                break
            index += 1

        #Checks that the move is inside the play area
        if new_pos.x <= 8 and new_pos.x >= 1 and new_pos.y <= 8 and new_pos.y >= 1:
            self.game_state[index].move(new_pos, self.game_state) 