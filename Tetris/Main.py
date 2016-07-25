
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

pygame.mixer.init()
# pygame.mixer.music.load('music2.mp3')
# pygame.mixer.music.play(-1)

menuMusic = pygame.mixer.Sound('music2.ogg')
gameMusic = pygame.mixer.Sound('music.ogg')
endMusic = pygame.mixer.Sound('music3.ogg')

menuMusic.play(-1)


# initialize pygame
pygame.init()
GREEN = (0, 255, 0)

# initialize a clock for the game, so you can control the framerate
clock = pygame.time.Clock()

# create a screen 
screen = pygame.display.set_mode((550, 525))
pygame.display.set_caption('Tetris Reborn')

# <<ADVANCED>> If you want KEYDOWN event to fire continuously, when a key is held down
# ============ give it two argument, both of them are interval of KEYDOWN event
pygame.key.set_repeat(50, 50)

import Menu
import GameLogic


#-------------------------
# Our Main Loop
#-------------------------
while True:
## Your must have one and only one big while loop for your game
## Each time the loop is executed, on framed
   # while GameLogic.state == GameLogic.gameState:
        #-------------------------
        # Our event hanlding loop
        #-------------------------
    eventList = pygame.event.get()
    # grab all events pygame recieved
    for event in eventList:
        if event.type == pygame.QUIT:
            
            exit()
        elif event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_q:
                GameLogic.state = GameLogic.endGameState
                gameMusic.fadeout(1000)
                endMusic.play(-1)
                print ('q pressed ')
            if event.key == pygame.K_m:
                GameLogic.state = GameLogic.menuState
                endMusic.fadeout(1000)
                gameMusic.stop()
                menuMusic.play(-1)

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
                GameLogic.tick = GameLogic.tickfast
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if GameLogic.state == GameLogic.menuState:
                if event.pos[0] >= 180 and event.pos[0] <= (180+200) and event.pos[1] >= (90) and event.pos[1] <= (90+50):
                    GameLogic.state = GameLogic.gameState
                    menuMusic.fadeout(1000)
                    gameMusic.play(-1)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                GameLogic.tick = GameLogic.permtick
            if event.key == pygame.K_RIGHT:
                GameLogic.tick = GameLogic.permtick
            if event.key == pygame.K_LEFT:
                GameLogic.tick = GameLogic.permtick

    GameLogic.updateGame()

    GameLogic.draw(screen)

    if GameLogic.state != GameLogic.endGameState and Graph.TGrid [0] != [0,0,0,0,0,0,0,0,0,0]:
        gameMusic.fadeout(1000)
        endMusic.play(-1)
        GameLogic.state = GameLogic.endGameState

 
    pygame.display.flip()
 
    clock.tick(GameLogic.tick)
 
    
        



        
        