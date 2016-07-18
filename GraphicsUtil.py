import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Grid
# ------------------------------

width = 25
winLen = 300
winWidth = 510
gridList = []
grid = pygame.Surface((winLen, winWidth))

def dot(x,y):
    pt = (x,y)
    return pt

for i in range (int(winLen/10) +1,int(winLen *9/10) + 1,width):
    for j in range (int(winWidth/20) +1,int(winWidth *17/20)+1,width):
        gridList.append(dot(i,j))
        
for i in range(len(gridList)):
        a = gridList[i]
        rect = pygame.Rect(a, (width, width))
        pygame.draw.rect(grid, (0,0,250), rect,2)
# set the background 
# ------------------------------
bckgdSurface = pygame.Surface((500,500))
bckgd = pygame.image.load("GalaxyBkgd.jpg")
bckgd = pygame.transform.scale(bckgd, (500,500))

bckgdSurface.blit(bckgd, (0,0))

# Square Block Object
# ------------------------------

