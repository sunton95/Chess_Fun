import sys, pygame
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((640, 480))
texture_pieces = pygame.image.load('Chess_Pieces_Sprite.png')

pawn = pygame.Surface((200,200))
pawn.blit(texture_pieces, (0, 0),(100,100,100,100))


objects = []

while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.blit(pawn, (10,10))
    pygame.display.update()
    pygame.time.delay(100)