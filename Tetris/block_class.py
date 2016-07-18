import pygame
from pygame import *
class Block:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color
        
    def draw(self):
        surface = pygame.Surface((self.length, self.width))
        pygame.draw.rect(surface, self.color, (0, 0, self.length, self.width))
        return surface
    
    

# if __name__ == "__main__":
#     pygame.init()
#     color = (0, 255, 0)

#     screen = pygame.display.set_mode((500, 500))

#     b = Block(25,25, color)
#     screen.fill((255, 255,255))
#     screen.blit(b.draw(), (250,250))
#     pygame.display.flip()
#     pygame.time.wait(1000)
