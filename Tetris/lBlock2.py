import pygame
from pygame import *
import block_class
from block_class import Block
from GraphicsUtil import toplength, topwidth

blockWidth = 25
x = 0
y = 0
YELLOW = (255, 255, 0)


lSurface = pygame.Surface((75,50))
lSurface.set_colorkey((0,0,0))


B1 = Block(blockWidth,blockWidth, YELLOW, x, y)
B2 = Block(blockWidth,blockWidth, YELLOW, x+1, y)
B3 = Block(blockWidth,blockWidth, YELLOW, x+2, y)
B4 = Block(blockWidth,blockWidth, YELLOW, x, y-1)

B1.groupDrawlBlock2(lSurface)
B2.groupDrawlBlock2(lSurface)
B3.groupDrawlBlock2(lSurface)
B4.groupDrawlBlock2(lSurface)


class lBlock2:
    def __init__(self):
       self.surface = lSurface
       self.rotate = 0
       
    def draw(self, screen,x,y):
        screen.blit(self.surface,(x*25+topwidth, y*25+toplength))

# while True:
#     if __name__ == "__main__":
#         pygame.init()
#         screen = pygame.display.set_mode((500, 500))
#         b = lBlock2()
#         screen.fill((255, 255,255))
#         b.draw(screen, 200, 200)

#         screen.blit(b, (200, 200))
#         eventList = pygame.event.get()
#         for event in eventList:
#             if event.type == pygame.QUIT:
#                     # if someone tries to close the Windows
#                     exit()

#         pygame.display.flip()        
       
