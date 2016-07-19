import pygame
from pygame import *
import block_class
from block_class import Block

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

B1.groupDraw(lSurface)
B2.groupDraw(lSurface)
B3.groupDraw(lSurface)
B4.groupDraw(lSurface)

class lBlock:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
    
    def draw(self, screen):
        screen.blit(lSurface, (self.xPos, self.yPos))
    

class lBlock2:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
    
    def draw(self, screen):
        screen.blit(pygame.transform.flip(lSurface, True, False), (self.xPos, self.yPos))

while True:
    if __name__ == "__main__":
        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        b = lBlock2(200,200)
        screen.fill((255, 255,255))
        b.draw(screen)

        screen.blit(b, (200, 200))
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                    if someone tries to close the Windows
                    exit()

        pygame.display.flip()        
       
