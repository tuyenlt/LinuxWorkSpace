import pygame,sys
from pygame.locals import *
from GameConfig import *

screen = pygame.display.set_mode((SRC_WIDTH, SRC_HEIGHT))

player = Rect(0,0,80,100)
gravity = -7
jumpspeed = 0
time = 0
movespeed = 2

while True:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumpspeed = 50
            if event.key == pygame.K_a:
                player.left -= movespeed 
            if event.key == pygame.K_d:
                player.left += movespeed 
                 
    pygame.display.update()
    screen.fill(COLOR_WHITE)
    pygame.draw.rect(screen,COLOR_LBLUE,player)

    if jumpspeed > 0 or player.bottom < 500:
        player.bottom -= jumpspeed
        jumpspeed += gravity
    if player.bottom > 500:
        player.bottom = 500
