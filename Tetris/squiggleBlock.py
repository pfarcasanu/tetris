import pygame
from pygame import *
import block_class
from block_class import Block
from GraphicsUtil import toplength, topwidth

blockWidth = 25
x = 0
y = 0

squiggleSurface = pygame.Surface((75,50))
squiggleSurface.set_colorkey((0,0,0))


B1 = Block(blockWidth,blockWidth, (0,255,255), x, y)

B1.groupDrawSquiggleBlock(squiggleSurface)


class squiggleBlock:
    def __init__(self):
        self.color = 5
        self.surface = squiggleSurface
        self.rotate = 0
        
    def points(self):
        if self.rotate%2==0:
            return [(0,1), (1,0), (2,0), (1,1)]
        if self.rotate%2==1:
            return [(0,0), (0,1), (1,1), (1,2)]
       



# while True:
#     if __name__ == "__main__":
#         pygame.init()
#         screen = pygame.display.set_mode((500, 500))
#         b = squiggleBlock2(200,200)
#         screen.fill((255, 255,255))
#         b.draw(screen)

#         # screen.blit(b, (200, 200))
#         eventList = pygame.event.get()
#         for event in eventList:
#             if event.type == pygame.QUIT:
#                     # if someone tries to close the Windows
#                     exit()

#         pygame.display.flip()        
       
