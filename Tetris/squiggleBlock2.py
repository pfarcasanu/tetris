import pygame
from pygame import *
import block_class
from block_class import Block
from GraphicsUtil import toplength, topwidth

blockWidth = 25
x = 0
y = 0

squiggleSurface2 = pygame.Surface((75,50))
squiggleSurface2.set_colorkey((0,0,0))


B1 = Block(blockWidth,blockWidth, (0,255,255), x, y)

B1.groupDrawSquiggleBlock2(squiggleSurface2)


class squiggleBlock2:
    def __init__(self):
        self.color = 6
        self.surface = squiggleSurface2
        self.rotate = 0      
    
    def points(self):   
        if self.rotate%2==0:
            return [(0,0), (1,0), (1,1), (2,1)]
        if self.rotate%2==1:
            return [(1,0), (0,1), (1,1), (0,2)]