import pygame,sys
from pygame.locals import *
import math

pygame.init()

WIDTH = 600
HEIGHT = 600

font = pygame.font.Font('freesansbold.ttf', 10)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
circle_radius = 0
get_point_mode = False
omega = math.pi
point_x = WIDTH/2
point_y = HEIGHT/2
time = 0
anpha = 0
fps = 120 
block_rect = Rect(WIDTH/2,HEIGHT/2,15,15)
omega_text = font.render("Omega: " +str(omega), True, BLUE)
radius_text = font.render('Radius: 0', True, BLUE)
anpha_text = font.render('anpha0: ' + str(anpha), True, BLUE)


while True:
    pygame.time.Clock().tick(fps)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            get_point_mode = True
        if event.type == MOUSEBUTTONUP:
            get_point_mode = False
            
            
    point_text = font.render('X:' + str(int(-point_x+mouse_x)) + ' Y: ' + str(int(mouse_y-point_y)), True, BLUE)
    pygame.display.update()
    screen.fill(WHITE)
    screen.blit(radius_text,(WIDTH - 100,HEIGHT -10))
    screen.blit(anpha_text,(WIDTH - 100,HEIGHT -30))
    screen.blit(point_text,(WIDTH - 100,HEIGHT -50))
    screen.blit(omega_text,(WIDTH - 100,HEIGHT -70))
    pygame.draw.circle(screen,RED,(WIDTH/2,HEIGHT/2),circle_radius,3)
    pygame.draw.line(screen,RED,(WIDTH/2-circle_radius,HEIGHT/2),(WIDTH/2 + circle_radius,HEIGHT/2),2)
    pygame.draw.line(screen,RED,(WIDTH/2,HEIGHT/2-circle_radius),(WIDTH/2,HEIGHT/2 + circle_radius),2)
    pygame.draw.circle(screen,BLUE,(point_x,point_y),5,5)
    pygame.draw.rect(screen,BLUE,block_rect)
    pygame.draw.line(screen,RED,(point_x,point_y),(block_rect.center),2)
    pygame.draw.line(screen,RED,(point_x,point_y),(WIDTH/2,HEIGHT/2),2)
    if get_point_mode:
        time = 0
        point_x = mouse_x
        point_y = mouse_y
        block_rect.center = (point_x,HEIGHT/2)
        radius_x = math.pow((mouse_x - WIDTH/2),2)
        radius_y = math.pow((mouse_y - HEIGHT/2),2)
        circle_radius = math.sqrt(radius_x + radius_y)
        if circle_radius > 0: 
            anpha = math.acos((mouse_x -  WIDTH/2)/circle_radius)
        if mouse_y > HEIGHT/2: anpha = -anpha
        
        radius_text = font.render('Radius: ' + str(int(circle_radius)), True, BLUE)
        anpha_text = font.render('anpha: ' + str(anpha), True, BLUE)
    else:
        point_x = WIDTH/2 + circle_radius*math.cos(omega*time + anpha)
        point_y = WIDTH/2 - circle_radius*math.sin(omega*time + anpha)
        block_rect.center = block_rect.center = (point_x,HEIGHT/2)
        time += 1/fps