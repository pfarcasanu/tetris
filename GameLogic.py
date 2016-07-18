import pygame
import GraphicsUtil as Graph


# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    pass


# A method that does all the drawing for you.
def draw(screen):
    # setup a differnt background, 
    screen.fill(Graph.BLACK)
    # copy the image of hero to the screen at the cordinate of hero
    screen.blit(Graph.grid, (0, 0))

    screen.blit(Graph.scoreSurface, (285, 200))