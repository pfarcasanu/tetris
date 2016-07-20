import pygame
pygame.font.init()

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
grid.set_colorkey(BLACK)


#toplength etc
toplength = int(winLen/10) +1
bottomlength = int(winLen *9/10) + 1
topwidth = int(winWidth/10) +1
bottomwidth = int(winWidth *9/10)+1

def dot(x,y):
    pt = (x,y)
    return pt

for i in range (toplength,bottomlength,width):
    for j in range (topwidth,bottomwidth,width):
        gridList.append(dot(i,j))
        
for i in range(len(gridList)):
        a = gridList[i]
        rect = pygame.Rect(a, (width, width))
        pygame.draw.rect(grid, (WHITE), rect,2)
TGrid = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

# fdasfsa
# ------------------------------

# set the background 
# ------------------------------

# bckgd = pygame.image.load("GalaxyBkgd.jpg")
# bckgd = pygame.transform.scale(bckgd, (500,500))
# bckgd.blit(bckgd, (0,0))

# Score Box
# ------------------------------
scoreSurface = pygame.Surface((200, 50))
scoreImage = pygame.image.load("ScoreBox.png")
scoreImage = pygame.transform.scale(scoreImage, (200, 50))
scoreSurface.blit(scoreImage, (0, 0))

scoreWordSurface = pygame.Surface((200, 50))
scoreWordBox = pygame.image.load("ScoreWord.png")
scoreWordBox = pygame.transform.scale(scoreWordBox, (200, 50))
scoreWordSurface.blit(scoreWordBox, (0, 0))

# Next Box
nextSurface = pygame.Surface((200, 50))
nextWordBox = pygame.image.load("NextBlock.png")
nextWordBox = pygame.transform.scale(nextWordBox, (200, 50))
nextSurface.blit(nextWordBox, (0, 0))
 #Next Show Box
nextShowSurface = pygame.Surface((200, 200))
nextShowBox = pygame.image.load("NextBlockShow.png")
nextShowBox = pygame.transform.scale(nextShowBox, (200, 200))
nextShowSurface.blit(nextShowBox, (0, 0))

# Square Tetramino 
#-------------------

#Tetra
