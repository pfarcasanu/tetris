import pygame
import block_class
from block_class import Block

blockWidth = 25
squareXpos = 0
squareYpos = 0

squareSurface = Surface((60,60))

B1 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos)
B2 = Block(blockWidth,blockWidth, (255,0,0), squareXpos+ blockWidth, squareYpos)
B3 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos+blockWidth)
B4 = Block(blockWidth,blockWidth, (255,0,0), squareXpos+blockWidth, squareYpos+blockWidth)

B1.draw(squareSurface)
B2.draw(squareSurface)
B3.draw(squareSurface)
B4.draw(squareSurface)

class squareBlock:
    def __init__(self, xPos, yPos)
        self.xPos = xPos
        self.yPos = yPos
    
    def draw(self, screen):
        screen.blit(squareSurface, (self.xPos, self.yPos))
       