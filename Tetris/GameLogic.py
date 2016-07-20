import pygame
import random
import GraphicsUtil as Graph

import block_class
from block_class import Block

import squareBlock
from squareBlock import squareBlock

import lineBlock
from lineBlock import lineBlock

import lBlock
from lBlock import lBlock, lBlock2

import squiggleBlock
from squiggleBlock import squiggleBlock, squiggleBlock2

import Tblock
from Tblock import TBlock

#list of tetraminos
tetraminoList = [squiggleBlock, squiggleBlock2, lBlock, 
    lBlock2, squareBlock, lineBlock, Tblock]




BLACK = (0,0,0)
GREEN = (0, 255, 0)
x = 5
y = 0
ychange = 0


def randomeBlock():
    b = tetraminoList[random.randint(0, len(tetraminoList)-1)]
    return b()

# currentblock = randomeBlock()
currentblock = lineBlock()
    
    
# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    global x,y, ychange
    ychange += 1
    if ychange == 4:
        y+=1
        ychange = 0
    if Graph.TGrid[y+1][x] == 1 or y == 16:
        Graph.TGrid[y][x] = 1
   
   
# A method that flips the tetraminos
def rotate(tetramino):
    tetramino.surface = pygame.transform.rotate(tetramino.surface, 90)

# A method that keeps track of the block graphics
#def 


# A method that does all the drawing for you.
def draw(screen):
    global currentblock, y, x
    # setup a differnt background, 
    if Graph.TGrid[y+1][x] == 1 or y == 16:
        y = 0
        x = 5
        currentblock = randomeBlock()
    else:
        screen.fill(Graph.BLACK)
    screen.blit(Graph.grid, (0, 0))
    currentblock.draw(screen, x, y)

    for i in range (len(Graph.TGrid)):
        for j in range (len(Graph.TGrid[i])):
            if Graph.TGrid [i][j] == 1:
                Block(25, 25, GREEN, j, i).draw(screen)
                # currentblock.draw(screen, x ,y)


    # Clear a row when complete
    for i in Graph.TGrid:
        if i == [1,1,1,1,1,1,1,1,1,1]:
            Graph.TGrid.remove[1,1,1,1,1,1,1,1,1,1]
            Graph.TGrid.insert(0,[0,0,0,0,0,0,0,0,0,0])
                


    # Sq1 = squareBlock(200,200)
    # Sq1.draw(screen)
    
    # Line1 = lineBlock (100,100)
    # Line1.draw(screen)
    
        
       
    
    
    # Sq1 = squareBlock(0,0)
    # Sq1.draw(screen)
    
    screen.blit(Graph.scoreSurface, (285, 400))
    
    screen.blit(Graph.scoreWordSurface, (285, 330))
    
        # screen.blit(Graph.scoreWordSurface, (285, 330))
        # screen.blit(Graph.nextSurface, (285, 50))



