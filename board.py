# =============================================================================
# Created By  : Anton Sundqvist
# Created Date: 2021-12-13
"""This file has the functions of drawing the game on the GUI and initilize the 
setup of the game. """
# =============================================================================
# TODO
#
# =============================================================================
# Imports
from pieces.bishop import *
from pieces.king import *
from pieces.queen import *
from pieces.knight import *
from pieces.pawn import *
from pieces.rook import *
from postition import Position
from flags import Flags
import os
import pygame
# =============================================================================

class GameBoard:
    def __init__(self, move_number):
        self.game_state = []
        self.position_list = []
        self.move_number = move_number
        self.flags = Flags(False, False, False, False, False, False, False, False)

    #Uses the FEN foramting to set the board and initilize the flags indicating casteling and en passant
    def board_setup(self, FEN_string):
        pieces_on_board, side_to_move, casteling_ability, enpassant_target, half_clock, full_clock = FEN_string.split(' ')
        
        self.initialize_casteling(casteling_ability)
        self.initialize_move_number(side_to_move, half_clock, full_clock)
        self.initilize_pieces(pieces_on_board)

        if(enpassant_target != '-'):
            Pawn.en_passant_target = En_passant(Position.chess_notation_to_cord(enpassant_target), (self.move_number - 1))

    def initialize_casteling(self, casteling_ability):
        for char in casteling_ability:
            if(char == 'K'):
                self.flags.white_king_side_castling = True
            elif(char == 'Q'):
                self.flags.white_queen_side_castling = True
            elif(char == 'k'):
                self.flags.black_king_side_castling = True
            elif(char == 'q'):
                self.flags.black_queen_side_castling = True

    def initialize_move_number(self, side_to_move, half_clock, full_clock):
        move = int(full_clock)
        move = move * 2

        if side_to_move == 'w':
            self.move_number = move - 1
            Pawn.move_number = move - 1
        elif side_to_move == 'b':
            self.move_number = move
            Pawn.move_number = move


    def initilize_pieces(self, pieces_on_board):
        index = [1, 8]

        for pieces in pieces_on_board:
            if pieces == 'P':
                self.game_state.append(Pawn("White", index, 'P')) 
            elif pieces == 'R':
                self.game_state.append(Rook("White", index, 'R'))
            elif pieces == 'N':
                self.game_state.append(Knight("White", index, 'N'))
            elif pieces == 'B':
                self.game_state.append(Bishop("White", index, 'B'))
            elif pieces == 'Q':
                self.game_state.append(Queen("White", index, "Q"))
            elif pieces == 'K':
                self.game_state.append(King("White", index, "K"))
                King.white_king_position = Position(index[0], index[1]) 
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
                King.black_king_position = Position(index[0], index[1])  

            if pieces == "/":
                index[1] -= 1
                index[0] = 1
            elif pieces.isdigit() == True:
                index[0] = int(pieces) + index[0]
            else:
                index[0] += 1

    #Checks if a piece is clicked if it is it wont be drawn at its location. That pieces drawing is handled by draw_drag function
    def draw_pieces(self, screen, selected_piece):
        Pawn.move_number = self.move_number
        
        for pieces in self.game_state:
            if pieces != selected_piece:
                x = (pieces.position.x - 1) * 100
                y = 700 - ((pieces.position.y - 1) * 100)
                screen.blit(pieces.image, (x, y))

    #Loads each piece image and resizes it to 100px and returns a list with all images
    def init_images(self):

        black_pawn = pygame.image.load('images/black_pawn.png').convert_alpha()
        black_pawn = pygame.transform.scale(black_pawn, (100, 100))
        Pawn.image_black = black_pawn

        black_knight = pygame.image.load('images/black_knight.png').convert_alpha()
        black_knight = pygame.transform.scale(black_knight, (100, 100))
        Knight.image_black = black_knight

        black_rook = pygame.image.load('images/black_rook.png').convert_alpha()
        black_rook = pygame.transform.scale(black_rook, (100, 100))
        Rook.image_black = black_rook

        black_bishop = pygame.image.load('images/black_bishop.png').convert_alpha()
        black_bishop = pygame.transform.scale(black_bishop, (100, 100))
        Bishop.image_black = black_bishop

        black_queen = pygame.image.load('images/black_queen.png').convert_alpha()
        black_queen = pygame.transform.scale(black_queen, (100, 100))
        Queen.image_black = black_queen

        black_king = pygame.image.load('images/black_king.png').convert_alpha()
        black_king = pygame.transform.scale(black_king, (100, 100))
        King.image_black = black_king

        white_pawn = pygame.image.load('images/white_pawn.png').convert_alpha()
        white_pawn = pygame.transform.scale(white_pawn, (100, 100))
        Pawn.image_white = white_pawn

        white_knight = pygame.image.load('images/white_knight.png').convert_alpha()
        white_knight = pygame.transform.scale(white_knight, (100, 100))
        Knight.image_white = white_knight

        white_rook = pygame.image.load('images/white_rook.png').convert_alpha()
        white_rook = pygame.transform.scale(white_rook, (100, 100))
        Rook.image_white = white_rook

        white_bishop = pygame.image.load('images/white_bishop.png').convert_alpha()
        white_bishop = pygame.transform.scale(white_bishop, (100, 100))
        Bishop.image_white = white_bishop

        white_queen = pygame.image.load('images/white_queen.png').convert_alpha()
        white_queen = pygame.transform.scale(white_queen, (100, 100))
        Queen.image_white = white_queen

        white_king = pygame.image.load('images/white_king.png').convert_alpha()
        white_king = pygame.transform.scale(white_king, (100, 100))
        King.image_white = white_king

    def draw_background(self, screen):
        # Initialing Color for each square
        ch_1 = (238,238,210)
        ch_2 = (118,150,86)
        
        for x in range(0, 8):
            for y in range(0, 8):
                if ((y + x) % 2) == 0:
                    pygame.draw.rect(screen, ch_1, pygame.Rect((y * 100), (x * 100), 100, 100))
                else:
                    pygame.draw.rect(screen, ch_2, pygame.Rect((y * 100), (x * 100), 100, 100))

    def draw_drag(self, screen, selected_piece, game_state, flags):
        #Get the cordinate of the mouse so we know were the piece is dropped
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        x = int((mouse_pos[0] // 100) + 1)
        y = int(7 - (mouse_pos[1] // 100) + 1)
        
        #If a pieces is clicked the aviLble moves will be lit up and posistion of the clicked piece updated
        if selected_piece:
            if selected_piece.position.x != None:
                #Calculates the pixel location of the chess cordinates for drawing on game area
                pos_x = (selected_piece.position.x - 1 ) * 100
                pos_y = 700 - ((selected_piece.position.y - 1) * 100)
                rect = (pos_x, pos_y, 100, 100)
                pygame.draw.rect(screen, (0, 255, 0, 50), rect, 2)
        
            screen.blit(selected_piece.image, ((mouse_pos[0] - 50), (mouse_pos[1] - 50)))

            avilable_moves = selected_piece.move(None, game_state, flags)
            for move in avilable_moves:
                s = pygame.Surface((100,100), pygame.SRCALPHA)   # per-pixel alpha
                s.fill((255,0,0,128))                         # notice the alpha value in the color
                screen.blit(s, (((move.x - 1) * 100), ((700 - (move.y - 1) * 100))))

        #Returns a position where the mouse is and if the mouseclick is up it will be the new move
        return Position(x, y)

    #Function for drawing the game in terminal and ignoring the GUI. Not used as of now
    def draw_board_terminal(self):
        #Clears the terminal before printing a new frame of the game
        os.system('cls||clear')

        #Creates an empty list of all the positions on the board
        for x in range(0, 65):
            self.position_list.append(" ")

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

def mark_king():
    #print("CHECK")
    pass

def remove_spaces(string):
    list = [string[i:i+8] for i in range(0, len(string), 8)]
    temp_string = []
    fen_string = ''

    for row in list:
        for l in row:
            if(l == ' '):
                temp_string.append('1')
            else:
                temp_string.append(l)

        temp_string.reverse()
        temp_string.append('/')
        fen_string += ''.join(temp_string)
        temp_string.clear()

    return fen_string


def generate_fen_string(self):
    string = '                                                                '
    string = list(string)
    en_passant = None

    for piece in self.game_state:
        index = piece.position.convert_coordinates()
        string[index] = piece.label
        if(piece.label == 'p' or piece.label == 'P'):
            en_passant = piece

    fen_list = list(remove_spaces(''.join(string)))
    fen_list = fen_list[:-1]
    string = ''.join(fen_list)
    string = string[::-1]

    string = format_fen_string_remove_ones(string)

    if ((self.move_number) % 2) == 0:
        string += ' b '
        color = "black"
    elif((self.move_number) % 2) == 1:
        string += ' w '
        color = "white"

    #Casteling string
    castling = False
    if(self.flags.white_king_side_castling == True):
        string += 'K'
        castling = True
    if(self.flags.white_queen_side_castling == True):
        string += 'Q'
        castling = True
    if(self.flags.black_king_side_castling == True):
        string += 'k'
        castling = True
    if(self.flags.black_queen_side_castling == True):
        string += 'q'
        castling = True
    if(castling == False):
        string += '-'

    #Adds en passant string
    if(en_passant != None and en_passant.en_passant_target.move_number != None):
        if((en_passant.en_passant_target.move_number + 1) == self.move_number):
            string += ' ' + en_passant.en_passant_target.cord_change() + ' '
        else:
            string += ' - '
    else:
        string += ' - '

    string += '0 ' + str(((self.move_number + 1) // 2))

    return string

def format_fen_string_remove_ones(string):
    numeric_flag = False

    for x, l in enumerate(string):
        if(l.isnumeric()):
            if(numeric_flag == True):
                int_x = int(string[x])
                int_y = int(string[(x - 1)])
                string = string[:(x - 1)] + str(int_x + int_y) +  string[(x + 1):]
                break
            numeric_flag = True
        else:
            numeric_flag = False

    if("11" in string):
        string = format_fen_string_remove_ones(string)

    return string

if __name__ == "__main__":
    import main