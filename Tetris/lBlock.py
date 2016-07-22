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
        if self.rotate%4==1:
            return [(0,0), (0,1), (0,2), (1,2)]
        if self.rotate%4==2:
            return [(0,1), (1,1), (2,1), (2,0)]
        if self.rotate%4==3:
            return [(0,0), (1,0), (1,1), (1,2)]


# while True:
#     if __name__ == "__main__":
#         pygame.init()
#         screen = pygame.display.set_mode((500, 500))
#         # b = lBlock(200,200)
#         pygame.surface
#         screen.fill((255, 255,255))
#         b.draw(screen)

#         screen.blit(b, (200, 200))
#         eventList = pygame.event.get()
#         for event in eventList:
#             if event.type == pygame.QUIT:
                    
#                     exit()

#         pygame.display.flip()        
       
