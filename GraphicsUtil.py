import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Grid
# ------------------------------

width = 20
winLen = 300
winWidth = 510
gridList = []
grid = pygame.Surface((winLen, winWidth))

def dot(x,y):
    pt = (x,y)
    return pt

for i in range (int(winLen/10) +1,int(winLen *9/10) + 1,width):
    for j in range (int(winWidth/10) +1,int(winWidth *9/10)+1,width):
        gridList.append(dot(i,j))
        
for i in range(len(gridList)):
        a = gridList[i]
        rect = pygame.Rect(a, (width, width))
        pygame.draw.rect(grid, (0,0,250), rect,2)

#Score Block        
# ------------------------------
scoreSurface = pygame.Surface((200, 50))

scoreImage = pygame.image.load("C:/Users/floro/Desktop/Python Programs/Tetris-Rose-Hulman-Project/ScoreBox.png")
scoreImage = pygame.transform.scale(scoreImage, (200, 50))

scoreSurface.blit(scoreImage, (0, 0))

