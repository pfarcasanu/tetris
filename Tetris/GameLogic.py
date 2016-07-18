import pygame
import GraphicsUtil as Graph
import block_class
from block_class import Block
from GraphicsUtil import toplength
GREEN = (0, 255, 0)
x = 5
y = 0

# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    pass

# A method that keeps track of the block graphics
#def 


# A method that does all the drawing for you.
def draw(screen):
    # setup a differnt background, 
    # screen.fill(Graph.BLACK)
    # draw the graph 
    screen.blit(Graph.bckgdSurface, (0,0))
    screen.blit(Graph.grid, (0, 0))
<<<<<<< HEAD:Tetris/GameLogic.py
    b = Block(25,25, GREEN)
    Graph.grid.blit(b.draw(), (x*30,y*30+toplength))



    
=======

    screen.blit(Graph.scoreSurface, (285, 200))
>>>>>>> 7951fd5e7acfe6446d444d9702c594eefa6831c4:GameLogic.py
