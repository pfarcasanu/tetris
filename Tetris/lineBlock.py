import pygame
from pygame import *
import block_class
from block_class import Block

blockWidth = 25
lineXpos = 0
lineYpos = 0

BLUE = (0,0,255)

lineSurface = Surface((200,200))
lineSurface.set_colorkey((0,0,0))

B2 = Block(blockWidth,blockWidth, BLUE, lineXpos, lineYpos)
B1 = Block(blockWidth,blockWidth, BLUE, lineXpos, lineYpos+1)
B3 = Block(blockWidth,blockWidth, BLUE, lineXpos, lineYpos+2)
B4 = Block(blockWidth,blockWidth, BLUE, lineXpos, lineYpos+3)

B1.draw(lineSurface)
B2.draw(lineSurface)
B3.draw(lineSurface)
B4.draw(lineSurface)

class lineBlock:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
    
    def draw(self, screen):
        screen.blit(lineSurface, (self.xPos, self.yPos))


       
 