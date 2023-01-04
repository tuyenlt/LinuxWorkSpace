import pygame
from pygame.locals import *
from GameConfig import *

class PLayer():
    def __init__(self,spawn_x,spawn_y,height,width):
        self.rect = Rect(spawn_x,spawn_y,height,width)
        self.image = None
        self.jumpping = False
                
    def set_image(self,imagepath):
        self.image = pygame.image.load(imagepath)
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
    
    def eventHandle(self,event = pygame.event):
        pass
    
    def jump(self):
        pass    
    
    def display(self,surface):
        if self.image == None:
            pygame.draw.rect(surface,COLOR_LBLUE,self.rect)
        else:
            surface.blit(self.image, self.rect)
        
        