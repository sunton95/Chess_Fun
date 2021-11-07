from pieces import *
import os

class GameBoard:
    def __init__(self):
        self.game_state = []
        self.position_list = []

    def board_setup(self, FEN_string):
        FEN_string  = FEN_string.split(' ')
        pieces_on_board = FEN_string[0]

        index = [1, 1]

        for pieces in pieces_on_board:
            # match pieces:
            #     case 'p':
            #         self.game_state.append(Pawn("Black", index, "p")) 
            #     case 'r':
            #         self.game_state.append(Rook("Black", index, "r")) 
            #     case 'n':
            #         self.game_state.append(Knight("Black", index, "n"))         
            #     case 'b':
            #         self.game_state.append(Bishop("Black", index, "b")) 
            #     case 'q':
            #         self.game_state.append(Queen("Black", index, "q")) 
            #     case 'k':
            #         self.game_state.append(King("Black", index, "k"))  
            #     case 'P':
            #         self.game_state.append(Pawn("White", index, "P")) 
            #     case 'R':
            #         self.game_state.append(Rook("White", index, "R"))
            #     case 'N':
            #         self.game_state.append(Knight("White", index, "N"))
            #     case 'B':
            #         self.game_state.append(Bishop("White", index, "B"))
            #     case 'Q':
            #         self.game_state.append(Queen("White", index, "Q"))
            #     case 'K':
            #         self.game_state.append(King("White", index, "K"))

            if pieces == "/":
                index[1] += 1
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
        for x in range(0, 65):
            self.position_list.append(" ")
        for pieces in self.game_state:
            self.position_list[pieces.position.convert_coordinates()] = pieces.label
            
        print("\033[%d;%dH" % (1, 1))
        for x in range(1,9):
            i = 8 * (x - 1)
            print("|{}|{}|{}|{}|{}|{}|{}|{}|  {}".format(self.position_list[0 + i],
                                                         self.position_list[1 + i],
                                                         self.position_list[2 + i],
                                                         self.position_list[3 + i],
                                                         self.position_list[4 + i],
                                                         self.position_list[5 + i],
                                                         self.position_list[6 + i],
                                                         self.position_list[7 + i],                                                   
                                                         (9 - x)))

        print("")
        print("|{}|{}|{}|{}|{}|{}|{}|{}|".format("A","B","C","D","E","F","G", "H"))
        print("")
    
    def move_piece(self):
        pass