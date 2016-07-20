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
B4 = Block(blockWidth,blockWidth, YELLOW, x, y+1)

B1.groupDrawlBlock(lSurface)
B2.groupDrawlBlock(lSurface)
B3.groupDrawlBlock(lSurface)
B4.groupDrawlBlock(lSurface)

class lBlock:
    def __init__(self):
        self.surface = lSurface
        self.rotate = 0
    
    def draw(self, screen, x, y):
        screen.blit(self.surface, (x*25+toplength, y*25+topwidth))
    


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
       
