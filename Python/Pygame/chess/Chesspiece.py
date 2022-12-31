import pygame
from broad import *

class Chesspiece():
    def __init__(self,spawn_x,spawn_y,size = 100,side = "white"):
        self.pos_x = spawn_x
        self.pos_y = spawn_y
        self.size = size
        self.side = side
        self.image = pygame.image.load("lib/white_pawn.png")
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
        self.on_click = False
        self.move_able_pos = []
    
    def collidepoint(self,point_x,point_y):
        if self.rect.collidepoint(point_x,point_y):
            return True
        else : 
            return False
        
    def move_to(self,pos_x,pos_y):
        self.rect.center = (pos_x,pos_y)
    
    def get_move_able_pos(self,broad = ChessBroad):
        pass
    
    def display(self,br = ChessBroad(),pos_x = None,pos_y = None):
        if pos_x and pos_y != None:
            self.rect.center = (pos_x,pos_y)
        br.broad_sur.blit(self.image,self.rect)
        if self.on_click :
            for (x,y) in self.move_able_pos:
                pygame.draw.circle(br.broad_sur, COLOR_GREY, (x,y), 15 , 3)
    
        
class Pawn(Chesspiece):
    def __init__(self,spawn_x = 0,spawn_y = 0,size = 100,side = "white",):
        super().__init__(spawn_x,spawn_y,size,side)
        self.image = pygame.image.load("lib" + self.side + "_pawn.png")
        self.image = pygame.transform.scale(self.image,(self.size,self.size))
        self.rect = self.image.get_rect()
        
    def get_move_able_pos(self, broad=ChessBroad):
        if self.side == "black":
            if broad.box[self.pos_x][self.pos_y+1].placed:
                
                if broad.box[self.pos_x-1][self.pos_y+1].
    