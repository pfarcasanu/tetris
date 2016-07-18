import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Grid
# ------------------------------

width = 30
winLen = 300
winWidth = 510
gridList = []
grid = pygame.Surface((winLen, winWidth))
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
        pygame.draw.rect(grid, (0,0,250), rect,2)
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
        [0,0,0,0,0,0,0,0,0,0]]

# fdasfsa
# ------------------------------
# set the background 
# ------------------------------
bckgdSurface = pygame.Surface((500,500))
# bckgd = pygame.image.load("C:/Users/catapult.-PC/Documents/GitHub/Tetris-Rose-Hulman-Project/Tetris/GalaxyBkgd.jpg")
# bckgd = pygame.transform.scale(bckgd, (500,500))

# bckgdSurface.blit(bckgd, (0,0))

# Square Block Object
# ------------------------------
scoreSurface = pygame.Surface((200, 50))

# scoreImage = pygame.image.load("C:/Users/floro/Desktop/Python Programs/Tetris-Rose-Hulman-Project/ScoreBox.png")
# scoreImage = pygame.transform.scale(scoreImage, (200, 50))

# scoreSurface.blit(scoreImage, (0, 0))

