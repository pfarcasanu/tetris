import pygame
from pygame import *
import block_class
from block_class import Block

blockWidth = 25
lineXpos = 0
lineYpos = 0

BLUE = (0,0,255)

lineSurface = Surface((25,100))
lineSurface.set_colorkey((0,0,0))

B2 = Block(blockWidth,blockWidth, BLUE, lineXpos, lineYpos)
B1 = Block(blockWidth,blockWidth, BLUE, lineXpos, lineYpos+1)
B3 = Block(blockWidth,blockWidth, BLUE, lineXpos, lineYpos+2)
B4 = Block(blockWidth,blockWidth, BLUE, lineXpos, lineYpos+3)

B1.groupDrawLineBlock(lineSurface)
B2.groupDrawLineBlock(lineSurface)
B3.groupDrawLineBlock(lineSurface)
B4.groupDrawLineBlock(lineSurface)

class lineBlock:
    def __init__(self):
        self.surface = lineSurface
    
    def draw(self, screen, x, y):
        screen.blit(self.surface, (x*25, y*25))

# while True:
#     if __name__ == "__main__":
#         pygame.init()
#         screen = pygame.display.set_mode((500, 500))
#         b = lineBlock(200,200)
#         screen.fill((255, 255,255))
#         b.draw(screen)

#         # screen.blit(b, (200, 200))
#         eventList = pygame.event.get()
#         for event in eventList:
#             if event.type == pygame.QUIT:
#                     # if someone tries to close the Windows
#                     exit()

#         pygame.display.flip()
    

       
 