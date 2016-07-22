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
# tetraminoList = [lBlock, lBlock2, squareBlock, lineBlock,
#         squiggleBlock, squiggleBlock2, TBlock]

tetraminoList = [TBlock]


font = pygame.font.Font(None,36)




BLACK = (0,0,0)
GREEN = (0, 255, 0)
x = 4
y = 0
ychange = 0
score = 0


def randomeBlock():
    global x, y
    x,y = 4, 0
    b = tetraminoList[random.randint(0, len(tetraminoList)-1)]
    return b()

currentblock = randomeBlock()
# currentblock = squareBlock()
    
#a method that checks collisions
def checkCollision():
    pts = currentblock.points()
    for p in pts:
        px, py = x+p[0], y+p[1]
        if px<0 or px>= len(Graph.TGrid[0]):
            return True
        if py<0 or py>= len(Graph.TGrid) - 1:
            return True
        if Graph.TGrid [py][px] != 0:
            return True
    return False

#a method that checks collisions
def land():
    global currentblock
    pts = currentblock.points()
    for p in pts:
        px, py = x+p[0], y+p[1]
        Graph.TGrid[py][px] = currentblock.color
    print (pts)
    currentblock = randomeBlock()

    

# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    global currentblock, x,y, ychange
    ychange += 1
    if ychange == 4:
        y+=1
        if checkCollision():
            y-=1
            print ("check collision called")
            land()
        ychange = 0

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
    screen.fill(Graph.BLACK)
    screen.blit(Graph.gridGraphicSurface, (0, 0))  
    screen.blit(Graph.grid, (0, 0))

    pts = currentblock.points()
    for p in pts:
        px, py = x+p[0], y+p[1]
        screen.blit(currentblock.surface, (px*25+Graph.toplength, py*25+Graph.topwidth))

    for i in range (len(Graph.TGrid)):
        for j in range (len(Graph.TGrid[i])):
            loc = Graph.TGrid [i][j]
            if loc != 0:
                if loc == 1:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.yellowBlock)
                elif loc == 2:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.tealBlock)
                elif loc == 3:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.redBlock)
                elif loc == 4:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.greenBlock)
                elif loc == 5:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.blueBlock)
                elif loc == 6:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.orangeBlock)
                elif loc == 7:
                    b = Block(25,25, (255,0,0), j, i)
                    b.indBlock(screen,block_class.purpleBlock)



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



