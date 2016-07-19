import pygame
from pygame import *
import GraphicsUtil as Graph

blueBlock = pygame.image.load("Blue Block.png")
blueBlock = pygame.transform.scale(blueBlock, (25,25))




class Block:
    def __init__(self, length, width, color, x,y):
        self.length = length
        self.width = width
        self.color = color
        self.x = x
        self.y = y
        
    def draw(self, surface):

        print(self.x, self.y)
        # pygame.draw.rect(surface, self.color, (self.x*25, self.y*25, self.length,  self.width))

        pygame.draw.rect(surface, self.color, (self.x*25+Graph.toplength, self.y*25+Graph.topwidth,self.length, self.width))
    
    def groupDrawSquiggleBlock(self, surface):
        print(self.x, self.y)
        # pygame.draw.rect(surface, self.color, (self.x*25, self.y*25,self.length, self.width))
        surface.blit(blueBlock, (self.x*25, self.y*25))
    
    def groupDrawlBlock(self, surface):
        print(self.x, self.y)
        # pygame.draw.rect(surface, self.color, (self.x*25, self.y*25,self.length, self.width))
        surface.blit(blueBlock, (self.x*25, self.y*25))


    #def update(self):
    #     self.y +=1
    #     pygame.time.wait(500)
        
    

if __name__ == "__main__":
    pygame.init()
    color = (0, 255, 0)

    screen = pygame.display.set_mode((500, 500))

    b = Block(25,25, color)
    screen.fill((255, 255,255))
    screen.blit(b.draw(), (250,250))
    pygame.display.flip()
    pygame.time.wait(1000)
