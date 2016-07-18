import pygame
from pygame import *
import GraphicsUtil as Graph

class Block:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color
        
    def draw(self, grid, x,y):
        pygame.draw.rect(grid, self.color, (x*30, y*30+Graph.topwidth,self.length, self.width))
        
    
    

# if __name__ == "__main__":
#     pygame.init()
#     color = (0, 255, 0)

#     screen = pygame.display.set_mode((500, 500))

#     b = Block(25,25, color)
#     screen.fill((255, 255,255))
#     screen.blit(b.draw(), (250,250))
#     pygame.display.flip()
#     pygame.time.wait(1000)
