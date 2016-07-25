import pygame
from pygame import *
import block_class
from block_class import Block
from GraphicsUtil import toplength, topwidth
import GraphicsUtil as Graph

blockWidth = 25
x = 0
y = 0
YELLOW = (255, 255, 0)


lSurface = pygame.Surface((75,50))
lSurface.set_colorkey((0,0,0))

B1 = Block(blockWidth,blockWidth, YELLOW, x, y)
B1.groupDrawlBlock(lSurface)

class lBlock:
    def __init__(self):
        self.color = 3
        self.surface = lSurface
        self.rotate = 0
    
    def points(self):
        if self.rotate%4==0:
            return [(0,0), (1,0), (2,0), (0,1)]
        if self.rotate%4==3:
            return [(0,0), (0,1), (0,2), (1,2)]
        if self.rotate%4==2:
            return [(0,1), (1,1), (2,1), (2,0)]
        if self.rotate%4==1:
            return [(0,0), (1,0), (1,1), (1,2)]


