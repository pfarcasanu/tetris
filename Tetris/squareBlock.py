import pygame
from pygame import *
import block_class
from block_class import Block

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

class squareBlock:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
    
    def draw(self, screen):
        squareSurface = pygame.Surface((600,600))

        # squareSurface.set_colorkey((0,0,0))


        B1 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos)
        B2 = Block(blockWidth,blockWidth, (255,0,0), squareXpos+ 1, squareYpos)
        B3 = Block(blockWidth,blockWidth, (255,0,0), squareXpos, squareYpos+1)
        B4 = Block(blockWidth,blockWidth, (255,0,0), squareXpos+1, squareYpos+1)

        B1.draw(squareSurface)
        B2.draw(squareSurface)
        B3.draw(squareSurface)
        B4.draw(squareSurface)
        
        screen.blit(squareSurface, (self.xPos, self.yPos))
       

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    b = squareBlock(200,200)
    screen.fill((255, 255,255))
    b.draw(screen)

    # screen.blit(b, (200, 200))

    pygame.display.flip()
    pygame.time.wait(6000)

