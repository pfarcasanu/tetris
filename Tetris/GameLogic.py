import pygame
import random
import GraphicsUtil as Graph

import block_class
from block_class import Block

# import squareBlock
from squareBlock import squareBlock

# import lineBlock
from lineBlock import lineBlock

# import lBlock
from lBlock import lBlock

# import squiggleBlock
from squiggleBlock import squiggleBlock

# import Tblock
from Tblock import TBlock

#import squiggleBlock2
from squiggleBlock2 import squiggleBlock2

from lBlock2 import lBlock2

#list of tetraminos
# tetraminoList = [squiggleBlock, squiggleBlock2, squiggleBlock, lBlock, 
#     lBlock2, lBlock, squareBlock, lineBlock, TBlock]


tetraminoList = [TBlock]


tetraminoList = [squareBlock, lineBlock]


tetraminoList = [lineBlock, squareBlock]
font = pygame.font.Font(None,36)

tetraminoList = [lineBlock, lBlock]


tetraminoList = [lineBlock, lBlock, lBlock2, squareBlock, squiggleBlock]



font = pygame.font.Font(None,36)


BLACK = (0,0,0)
GREEN = (0, 255, 0)
x = 4
y = 0
ychange = 0
score = 0


def randomeBlock():
    b = tetraminoList[random.randint(0, len(tetraminoList)-1)]
    return b()

currentblock = randomeBlock()
# currentblock = squareBlock()
    
    
# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    global currentblock, x,y, ychange
    ychange += 1
    if ychange == 4:
        y+=1
        ychange = 0
    if isinstance(currentblock, squareBlock): 
        if Graph.TGrid[y+2][x] != 0 or Graph.TGrid[y+2][x+1] != 0 or y == 15:
            Graph.TGrid[y+1][x] = 1
            Graph.TGrid[y+1][x+1] = 1
            Graph.TGrid[y][x+1] = 1
            Graph.TGrid[y][x] = 1

    if isinstance(currentblock, lineBlock): 
        if currentblock.rotate%2==0:   
            if Graph.TGrid[y+4][x] != 0 or y == 13:
                Graph.TGrid[y+3][x] = 2
                Graph.TGrid[y+2][x] = 2
                Graph.TGrid[y+1][x] = 2
                Graph.TGrid[y][x] = 2
        else:
            if Graph.TGrid[y+1][x+3] != 0 or Graph.TGrid[y+1][x+2]!=0 or Graph.TGrid[y+1][x+1]!=0 or Graph.TGrid[y+1][x] != 0 or y == 16:
                Graph.TGrid[y][x+3] = 2
                Graph.TGrid[y][x+2] = 2
                Graph.TGrid[y][x+1] = 2
                Graph.TGrid[y][x] = 2

    if isinstance(currentblock, lBlock): 
        if currentblock.rotate%4==0:  
            if Graph.TGrid[y+2][x] != 0 or Graph.TGrid[y+1][x+1] != 0 or Graph.TGrid[y+1][x+2] != 0 or y == 15:
                Graph.TGrid[y][x] = 3
                Graph.TGrid[y][x+1] = 3
                Graph.TGrid[y][x+2] = 3
                Graph.TGrid[y+1][x] = 3
        elif currentblock.rotate%4==1: 
            if Graph.TGrid[y+3][x] != 0 or Graph.TGrid[y+3][x+1] != 0 or y == 14:
                Graph.TGrid[y][x] = 3
                Graph.TGrid[y+1][x] = 3
                Graph.TGrid[y+2][x] = 3
                Graph.TGrid[y+2][x+1] = 3
        elif currentblock.rotate%4==2: 
            if Graph.TGrid[y+1][x] != 0:
                y = 0
                x = 4
            if Graph.TGrid[y+2][x] != 0 or Graph.TGrid[y+2][x+1] != 0 or Graph.TGrid[y+2][x+2] != 0 or y == 15:
                Graph.TGrid[y+1][x] = 3
                Graph.TGrid[y+1][x+1] = 3
                Graph.TGrid[y+1][x+2] = 3
                Graph.TGrid[y][x+2] = 3
                
        else:
            if Graph.TGrid[y+1][x] != 0 or Graph.TGrid[y+3][x+1] != 0 or y == 14:
                Graph.TGrid[y][x] = 3
                Graph.TGrid[y][x+1] = 3
                Graph.TGrid[y+1][x+1] = 3
                Graph.TGrid[y+2][x+1] = 3

        
    if isinstance(currentblock, lBlock2): 
        if currentblock.rotate%2==0:
            if Graph.TGrid[y+2][x] != 0 or Graph.TGrid[y+2][x+1] != 0 or Graph.TGrid[y+2][x+2] != 0 or y == 15:
                Graph.TGrid[y+1][x] = 4
                Graph.TGrid[y+1][x+1] = 4
                Graph.TGrid[y+2][x+2] = 4
                Graph.TGrid[y][x] = 4
        if currentblock.rotate%2==1: 
            if Graph.TGrid[y+1][x] != 0:
                y = 0
                x = 5
            if Graph.TGrid[y+2][x] != 0 or Graph.TGrid[y+2][x+1] != 0 or Graph.TGrid[y+2][x+2] != 0 or y == 15:
                Graph.TGrid[y+1][x] = 4
                Graph.TGrid[y+1][x+1] = 4
                Graph.TGrid[y+1][x+2] = 4
                Graph.TGrid[y][x+2] = 4
        if currentblock.rotate%2==2:
            if Graph.TGrid[y+2][x] != 0 or Graph.TGrid[y+2][x+1] != 0 or Graph.TGrid[y+2][x+2] != 0 or y == 15:
                Graph.TGrid[y+1][x] = 4
                Graph.TGrid[y+1][x+1] = 4
                Graph.TGrid[y+1][x+2] = 4
                Graph.TGrid[y][x+2] = 4
        else:
            if Graph.TGrid[y+3][x] != 0 or Graph.TGrid[y+1][x+1] != 0 or y == 15:
                Graph.TGrid[y][x] = 4
                Graph.TGrid[y+1][x] = 4
                Graph.TGrid[y+2][x] = 4
                Graph.TGrid[y][x+1] = 4
    if isinstance(currentblock, squiggleBlock): 
        if currentblock.rotate%2==0 or rotate%2==2:
            if Graph.TGrid[y+1][x] != 0 or Graph.TGrid[y+2][x+1] != 0 or Graph.TGrid[y+2][x+2] != 0 or y == 15:
                Graph.TGrid[y][x] = 5
                Graph.TGrid[y][x+1] = 5
                Graph.TGrid[y+1][x+1] = 5
                Graph.TGrid[y+1][x+2] = 5


# A method that flips the tetraminos
def rotate(tetramino):
    tetramino.surface = pygame.transform.rotate(tetramino.surface, 90)
    tetramino.rotate += 1
    
# A method that keeps track of the block graphics
#def 


# A method that does all the drawing for you.
def draw(screen):
    global currentblock, y, x
    # setup a different background, 
    if Graph.TGrid[y][x] != 0:
        y = 0
        x = 4
        currentblock = randomeBlock()


    else:
        screen.fill(Graph.BLACK)
    screen.blit(Graph.gridGraphicSurface, (0, 0))  

    screen.fill(Graph.BLACK)
    screen.blit(Graph.grid, (0, 0))

    screen.fill(Graph.BLACK)
    screen.blit(Graph.grid, (0, 0))

    screen.blit(Graph.gridGraphicSurface, (0, 0))  

    screen.blit(Graph.grid, (0, 0))

    screen.blit(Graph.grid, (0, 0))


    currentblock.draw(screen, x, y)

    for i in range (len(Graph.TGrid)):
        for j in range (len(Graph.TGrid[i])):
            loc = Graph.TGrid [i][j]
            if loc != 0:
                if loc == 1:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.yellowBlock)
                if loc == 2:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.tealBlock)
                if loc == 3:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.redBlock)
                if loc == 4:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.greenBlock)
                if loc == 5:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.blueBlock)



    # Clear a row and score when complete
    bonus = -50
    for i in Graph.TGrid:
        global score
        if 0 not in i:
            Graph.TGrid.remove(i)
            Graph.TGrid.insert(0,[0,0,0,0,0,0,0,0,0,0])
            score += 100
            bonus += 50
    if bonus >= 0:
        score += bonus
    text = font.render(str(score),1,(255,255,255))
                


    # Sq1 = squareBlock(200,200)
    # Sq1.draw(screen)
    
    # Line1 = lineBlock (100,100)
    # Line1.draw(screen)
    
        
       
    
    
    # Sq1 = squareBlock(0,0)
    # Sq1.draw(screen)
    

    #Draws Boxes On The Side
    screen.blit(Graph.scoreSurface, (325, 400))
    
    screen.blit(Graph.scoreWordSurface, (325, 330))
    
    screen.blit(text, (335,415))

    screen.blit(Graph.nextSurface, (325, 50))

    screen.blit(Graph.nextShowSurface, (325, 115))



    #Draws Box Behind Grid
    #screen.blit(Graph.gridGraphicSurface, (0, 0))  



