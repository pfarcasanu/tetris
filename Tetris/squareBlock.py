import pygame
from pygame import *
import block_class
from block_class import Block
from GraphicsUtil import toplength, topwidth

blockWidth = 25
squareXpos = 0
squareYpos = 0


squareSurface = pygame.Surface((50,50))

squareSurface.set_colorkey((0,0,0))

B1 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos)

B1.groupDrawSquareBlock(squareSurface)


class squareBlock:
    def __init__(self):
        self.color = 1
        self.surface = squareSurface
        self.rotate = 0

    def points(self):   
        return [(0,0), (1,1), (1,0), (0,1)]                       

    # def groundDraw: 


# if __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((500, 500))
#     b = squareBlock(200,200)
#     screen.fill((255, 255,255))
#     b.draw(screen)

#     # screen.blit(b, (200, 200))

#     pygame.display.flip()
#     pygame.time.wait(4000)

