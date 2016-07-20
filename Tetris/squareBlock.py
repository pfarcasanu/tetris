import pygame
from pygame import *
import block_class
from block_class import Block
from GraphicsUtil import toplength, topwidth

blockWidth = 25
squareXpos = 0
squareYpos = 0

# squareSurface = pygame.Surface((60,60))

# squareSurface = Surface((77,50))
# squareSurface.set_colorkey((0,0,0))


# B2 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos)
# B1 = Block(blockWidth,blockWidth, (255,0,0), squareXpos+ 1, squareYpos)
# B3 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos+1)
# B4 = Block(blockWidth,blockWidth, (255,0,0), squareXpos+1, squareYpos+1)

# B1.draw(squareSurface)
# B2.draw(squareSurface)
# B3.draw(squareSurface)
# B4.draw(squareSurface)


squareSurface = pygame.Surface((50,50))

squareSurface.set_colorkey((0,0,0))

B1 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos)
B2 = Block(blockWidth,blockWidth, (255,0,0), squareXpos+ 1, squareYpos)
B3 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos+1)
B4 = Block(blockWidth,blockWidth, (255,0,0), squareXpos+1, squareYpos+1)

B1.groupDrawSquareBlock(squareSurface)
B2.groupDrawSquareBlock(squareSurface)
B3.groupDrawSquareBlock(squareSurface)
B4.groupDrawSquareBlock(squareSurface)

class squareBlock:
    def __init__(self):
        self.surface = squareSurface
        self.rotate = 0
        
    def draw(self, screen, x ,y):
        
        screen.blit(self.surface, (x*25+toplength, y*25+topwidth))
       

# if __name__ == "__main__":
#     pygame.init()
#     screen = pygame.display.set_mode((500, 500))
#     b = squareBlock(200,200)
#     screen.fill((255, 255,255))
#     b.draw(screen)

#     # screen.blit(b, (200, 200))

#     pygame.display.flip()
#     pygame.time.wait(4000)

