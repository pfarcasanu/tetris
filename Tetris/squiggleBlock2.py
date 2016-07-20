import pygame
from pygame import *
import block_class
from block_class import Block

blockWidth = 25
x = 0
y = 0

squiggleSurface2 = pygame.Surface((75,50))
squiggleSurface2.set_colorkey((0,0,0))


B1 = Block(blockWidth,blockWidth, (0,255,255), x, y)
B2 = Block(blockWidth,blockWidth, (0,255,255), x-1, y)
B3 = Block(blockWidth,blockWidth, (0,255,255), x-1, y+1)
B4 = Block(blockWidth,blockWidth, (0,255,255), x-2, y+1)

B1.groupDrawSquiggleBlock(squiggleSurface2)
B2.groupDrawSquiggleBlock(squiggleSurface2)
B3.groupDrawSquiggleBlock(squiggleSurface2)
B4.groupDrawSquiggleBlock(squiggleSurface2)

class squiggleBlock2:
    def __init__(self):
        self.surface = squiggleSurface2
        self.rotate = 0
    
    def draw(self, screen, x,y):
        screen.blit(self.surface, (x*25, y*25))