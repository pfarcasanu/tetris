import pygame
from pygame import *
import GraphicsUtil as Graph

blueBlock = pygame.image.load("Blue Block.png")
blueBlock = pygame.transform.scale(blueBlock, (25,25))

redBlock = pygame.image.load("Red Block.png")
redBlock = pygame.transform.scale(redBlock, (25,25))

orangeBlock = pygame.image.load("Orange Block.png")
orangeBlock = pygame.transform.scale(orangeBlock, (25,25))

purpleBlock = pygame.image.load("Purple Block.png")
purpleBlock = pygame.transform.scale(purpleBlock, (25,25))

tealBlock = pygame.image.load("Teal Block.png")
tealBlock = pygame.transform.scale(tealBlock, (25,25))

yellowBlock = pygame.image.load("Yellow Block.png")
yellowBlock = pygame.transform.scale(yellowBlock, (25,25))

greenBlock = pygame.image.load("Green Block.png")
greenBlock = pygame.transform.scale(greenBlock, (25,25))






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
    
    #Squiggle Blocks
    def groupDrawSquiggleBlock(self, surface):
        print(self.x, self.y)
        # pygame.draw.rect(surface, self.color, (self.x*25, self.y*25,self.length, self.width))
        surface.blit(blueBlock, (self.x*25, self.y*25))

    def groupDrawSquiggleBlock2(self, surface):
        print(self.x, self.y)
        # pygame.draw.rect(surface, self.color, (self.x*25, self.y*25,self.length, self.width))
        surface.blit(orangeBlock, (self.x*25, self.y*25))
    
    #L Block
    def groupDrawlBlock(self, surface):
        print(self.x, self.y)
        # pygame.draw.rect(surface, self.color, (self.x*25, self.y*25,self.length, self.width))
        surface.blit(redBlock, (self.x*25, self.y*25))

    #L Block
    def groupDrawlBlock2(self, surface):
        print(self.x, self.y)
        # pygame.draw.rect(surface, self.color, (self.x*25, self.y*25,self.length, self.width))
        surface.blit(greenBlock, (self.x*25, self.y*25))

    #Line 
    def groupDrawLineBlock(self, surface):
        print(self.x, self.y)
        # pygame.draw.rect(surface, self.color, (self.x*25, self.y*25,self.length, self.width))
        surface.blit(tealBlock, (self.x*25, self.y*25))

    #T Block
    def groupDrawTBlock(self, surface):
        print(self.x, self.y)
        # pygame.draw.rect(surface, self.color, (self.x*25, self.y*25,self.length, self.width))
        surface.blit(purpleBlock, (self.x*25, self.y*25))

    #Square Block
    def groupDrawSquareBlock(self, surface):
        print(self.x, self.y)
        # pygame.draw.rect(surface, self.color, (self.x*25, self.y*25,self.length, self.width))
        surface.blit(yellowBlock, (self.x*25, self.y*25))


    #def update(self):
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
