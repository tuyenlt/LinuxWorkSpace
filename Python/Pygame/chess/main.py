import pygame,sys
from pygame.locals import *
from GameConfig import *
from broad import *
from Chesspiece import *


pygame.init()

screen = pygame.display.set_mode((SRC_WIDTH, SRC_HEIGHT))
mainbroad = ChessBroad(800)


while True:
    mouse_x,mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            for i in mainbroad.box:
                for j in i:
                    if j.rect.collidepoint(mouse_x,mouse_y-100):
                        j.clicked = True

    pygame.display.update()
    screen.fill(COLOR_WHITE)
    mainbroad.display(screen,0,100)
    