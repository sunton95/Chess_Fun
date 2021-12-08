import sys, pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((640, 480))
texture_pieces = pygame.image.load('Chess_Pieces_Sprite.png')


#A and B are the distance from the top left corner. This places the image on the surface A px down and B px left.
#C and D are the cropped part of the image from the top left corner. C px down, D px left.
#E and F define the image size.
#(A, B),(C,D,E,F))

pawn = pygame.Surface((400,400))
pawn.blit(texture_pieces, (0, 0),(0,0,400,400))


objects = []

while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.blit(pawn, (10,10))
    pygame.display.update()
    pygame.time.delay(100)