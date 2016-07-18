import pygame
from pygame import *
import GraphicsUtil as Graph

class Block:
    def __init__(self, length, width, color, x,y):
        self.length = length
        self.width = width
        self.color = color
        self.x = x
        self.y = y
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x*25, self.y*25+Graph.topwidth,self.length, self.width))
        
    # def update(self):
    #     self.y +=1
    #     pygame.time.wait(500)
        
    

# if __name__ == "__main__":
#     pygame.init()
#     color = (0, 255, 0)

#     screen = pygame.display.set_mode((500, 500))

#     b = Block(25,25, color)
#     screen.fill((255, 255,255))
#     screen.blit(b.draw(), (250,250))
#     pygame.display.flip()
#     pygame.time.wait(1000)
