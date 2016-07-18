import pygame
from pygame import *
import block_class
from block_class import Block

blockWidth = 25
squareXpos = 0
squareYpos = 0

<<<<<<< HEAD
squareSurface = pygame.Surface((60,60))
=======
squareSurface = Surface((50,50))
squareSurface.set_colorkey((0,0,0))
>>>>>>> origin/master

B2 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos)
B1 = Block(blockWidth,blockWidth, (255,0,0), squareXpos+ 1, squareYpos)
B3 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos+1)
B4 = Block(blockWidth,blockWidth, (255,0,0), squareXpos+1, squareYpos+1)

B1.draw(squareSurface)
B2.draw(squareSurface)
B3.draw(squareSurface)
B4.draw(squareSurface)

class squareBlock:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
    
    def draw(self, screen):
        screen.blit(squareSurface, (self.xPos, self.yPos))
       

# # if __name__ == "__main__":
# #     pygame.init()
# #     color = (0, 255, 0)

# #     screen = pygame.display.set_mode((500, 500))

# #     b = squareBlock(25,25)
# #     screen.fill((255, 255,255))
# #     b.draw(screen)
#     B1.draw(screen)    
#     B2.draw(screen)
#     B3.draw(screen)
#     B4.draw(screen)
# #     pygame.display.flip()
# #     pygame.time.wait(1000)