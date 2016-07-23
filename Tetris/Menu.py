import pygame
#from Main import screen
font = pygame.font.Font(None,36)
startGame = False

class Button:
    def __init__(self, text, screen, x, y, xbound, ybound):
        self.text = text
        self.x = x
        self.y = y
        self.screen = screen
        self.xbound = xbound
        self.ybound = ybound
    def draw(self,surface):
        text = font.render(self.text,1,(255,255,255))
        self.surface = surface
        self.screen.blit(self.surface,(self.x,self.y))
        bg = pygame.image.load("ScoreBox.png")
        bg = pygame.transform.scale(bg,(self.xbound,self.ybound))
        self.screen.blit(bg,(self.x,self.y))
        self.screen.blit(text,(self.x+self.xbound/(len(self.text)/1.8),self.y+10))
        pygame.display.flip()
    def mouseClick(self):
        if pygame.mouse.get_pos()[0] >= self.x and pygame.mouse.get_pos()[0] <= (self.x+self.xbound) and pygame.mouse.get_pos()[1] >= self.y and pygame.mouse.get_pos()[1] <= self.y+self.ybound:
            return True
        else:
            return False
    

#==============================================================================
# Buttons
#==============================================================================
playButton = pygame.Surface((200,50))

#==============================================================================
# Menu Loop
#==============================================================================
startbutton = Menu.Button("Play Game", screen, 200, 50, 200, 50)
while Menu.startGame == False:
    eventList = pygame.event.get()
    startbutton.draw(Menu.playButton)
    for event in eventList:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startbutton.mouseClick() == True:
                Menu.startGame = True
            else:
                Menu.startGame = False
        if event.type == pygame.QUIT:           
            exit()