
#-------------------------
# initialize pygame
#-------------------------
import pygame
import GraphicsUtil as Graph

import block_class
from block_class import Block
from squareBlock import squareBlock
from lBlock import lBlock
from squiggleBlock import squiggleBlock
from Tblock import TBlock
from squiggleBlock2 import squiggleBlock2
from lBlock2 import lBlock2
from lineBlock import lineBlock




pygame.init()

pygame.mixer.init()

pygame.mixer.music.load('music.mp3')

pygame.mixer.music.play(-1)



# initialize pygame
pygame.init()
GREEN = (0, 255, 0)
tick = 10
permtick = tick
tickfast = tick * 5
# initialize a clock for the game, so you can control the framerate
clock = pygame.time.Clock()

# create a screen 
screen = pygame.display.set_mode((550, 525))
pygame.display.set_caption('Tetris Reborn')

# <<ADVANCED>> If you want KEYDOWN event to fire continuously, when a key is held down
# ============ give it two argument, both of them are interval of KEYDOWN event
pygame.key.set_repeat(50, 50)

import GameLogic

#-------------------------
# Our Main Loop
#-------------------------
## Your must have one and only one big while loop for your game
## Each time the loop is executed, one framed
while True:
    #-------------------------
    # Our event hanlding loop
    #-------------------------
    eventList = pygame.event.get()
    # grab all events pygame recieved
    for event in eventList:
        # Just for this level, print the event out, so you can experiment with it
    
        # <event.type> type attribute of an event encodes the type of the event
        if event.type == pygame.QUIT:
            # if someone tries to close the Windows
            exit()
        elif event.type == pygame.KEYDOWN:
        #     # if someone presses some key
        #     # <event.key> key attribute of a key-down event encodes which key is pressed
        #     # move the block accordingly
            if event.key == pygame.K_UP:
                GameLogic.currentblock.rotate += 1
                if GameLogic.checkCollision():
                    GameLogic.currentblock.rotate -= 1
            if event.key == pygame.K_LEFT:
                GameLogic.x -= 1
                print(GameLogic.x)
                if GameLogic.checkCollision():
                    GameLogic.x += 1
                    print(GameLogic.x)
            if event.key == pygame.K_RIGHT:
                GameLogic.x += 1
                if GameLogic.checkCollision():
                    GameLogic.x -= 1
            if event.key == pygame.K_DOWN:
                tick = tickfast
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                tick = permtick
            if event.key == pygame.K_RIGHT:
                tick = permtick
            if event.key == pygame.K_LEFT:
                tick = permtick
        
         

    #-------------------------
    # The graphics block
    #-------------------------
    ## all the drawing happen in updateGame()
    GameLogic.draw(screen)

    #-------------------------
    # The main game logic block
    #-------------------------
    ## all the exciting interactive of objects happen in updateGame()
    # print(Graph.TGrid)
    GameLogic.updateGame()
    # print(GameLogic.x,GameLogic.y)
    
    #-------------------------
    # display this frame and wait 
    #-------------------------
    pygame.display.flip()
    # ask pygame to display everythong on the GUI
    
    clock.tick(tick)
    # set the framerate of the game to 60fps, i.e. 60 updates in one second
    
    if Graph.TGrid [0] != [0,0,0,0,0,0,0,0,0,0]:
        # print ('score')
        break
        
        