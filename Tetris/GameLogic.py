import pygame
import GraphicsUtil as Graph
import block_class
# from block_class import Block

# currentblock = None

GREEN = (0, 255, 0)
x = 5
y = 0

# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    global x,y
    y+=1
   
   
    

# A method that keeps track of the block graphics
#def 


# A method that does all the drawing for you.
def draw(screen):
    global currentblock
    # setup a differnt background, 
    screen.fill(Graph.BLACK)
    # draw the graph 
    # screen.blit(Graph.bckgdSurface, (0,0))
    screen.blit(Graph.grid, (0, 0))
    currentblock = block_class.Block(30,30, GREEN, x, y)
    currentblock.draw(screen)
    
   
    


    screen.blit(Graph.scoreSurface, (285, 400))

<<<<<<< HEAD

    screen.blit(Graph.scoreWordSurface, (285, 330))

    screen.blit(Graph.nextSurface, (285, 50))

=======
>>>>>>> origin/master
