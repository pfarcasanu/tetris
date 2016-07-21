import pygame
from pygame import *

gridList = []
width = 30
winLen = 300
winWidth = 510
win = pygame.display.set_mode((winLen,winWidth))
pygame.display.set_caption ('Tetris: Reborn')

def dot(x,y):
    pt = (x,y)
    return pt

for i in range (int(winLen/10) +1,int(winLen *9/10) + 1,width):
    for j in range (int(winWidth/10) +1,int(winWidth *9/10)+1,width):
        gridList.append(dot(i,j))


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
           exit() 
    for i in range(len(gridList)):
        a = gridList[i]
        rect = pygame.Rect(a, (width, width))
        pygame.draw.rect(win, (0,0,250), rect,2)
        
    display.flip()

    

# print (gridList)

