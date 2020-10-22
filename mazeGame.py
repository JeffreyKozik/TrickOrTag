'''
Nathan Nguyen, Bill Zhou, Jeff Kozik
HackerSociety
Trick-or-Tag
Program Description: Two-player tage
'''

import math #gets math commands
import pygame #pulls in pygame code
import sys #allows closing of pygame window at end of game
import random   #allows use of random commands

#initialize pygame module
pygame.init()

#open a window, set size
w = 680
h= int(16/20*w)
xu = (w/21)
yu = (h/17)

size = (w,h) #width, height
surface = pygame.display.set_mode(size)

#set title bar of window
pygame.display.set_caption("Trick or Treat Tag")

#color contents
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (100,100,100)
RED = (255,0,0)
BROWN = (150,45,62)
YELLOW = (255, 255, 0)

#initialize constants
playerOne = pygame.image.load("playerOne.png")
playerOneIt = pygame.image.load("scaryghost.png")
playerTwo = pygame.image.load("friendlypumpkin.png")
playerTwoIt = pygame.image.load("scarypumpkin.png")
playerOneShrinked = pygame.transform.scale(playerOne, (16,28))
playerTwoShrinked = pygame.transform.scale(playerTwo, (16,28))
playerOneShrinkedIt = pygame.transform.scale(playerOneIt, (16,28))
playerTwoShrinkedIt = pygame.transform.scale(playerTwoIt, (16,28))
playerOneRect = pygame.Rect(xu*1, yu*15, 16, 28)
playerTwoRect = pygame.Rect(xu*15, yu*1, 16, 28)
blueGemImage = pygame.image.load("candycorn.png")
blueGemStretched = pygame.transform.scale(blueGemImage,(32, 32))
orangeGemImage = pygame.image.load("orangegem.png")
orangeGemStretched = pygame.transform.scale(orangeGemImage,(32,32))
greenGemImage = pygame.image.load("greengem.png")
greenGemStretched = pygame.transform.scale(greenGemImage,(32,32))

#import sound for collecting gems
blueCollectSound = pygame.mixer.Sound("bluepickup.wav")
orangeCollectSound = pygame.mixer.Sound("orangepickup.wav")
greenCollectSound = pygame.mixer.Sound("greenpickup.wav")

#set up game timer
#every second, a userevent will be added to the event queue
pygame.time.set_timer(pygame.USEREVENT, 1000)

#initialize borders
#left border
b1 = pygame.Rect(0, 0, xu*1, yu*16)
#bottom border
b2 = pygame.Rect(0, yu*16, xu*20, yu*1)
#right border
b3 = pygame.Rect(xu*20, yu*2, xu*1, yu*17)
#top border
b4 = pygame.Rect(xu*1, 0, xu*19, yu*1)
#draw end rectangle
e1 = pygame.Rect(xu*20, 0, xu, yu*2)

borderWalls = [b1, b2, b3, b4,e1]

#initialize horizontal walls
h1 = pygame.Rect(xu*1, yu*4, xu*5, yu*1)
h2 = pygame.Rect(xu*1, yu*7, xu*5, yu*1)
h3 = pygame.Rect(xu, yu*11, xu*2, yu*1) 
h4 = pygame.Rect(xu*8, yu*13, xu*4, yu*1)
h5 = pygame.Rect(xu*7, yu*7, xu*2, yu*1)
h6 = pygame.Rect(xu*8, yu*4, xu*4, yu*1)
h7 = pygame.Rect(xu*18, yu*3, xu*3, yu*1)
h8 = pygame.Rect(xu*14, yu*6, xu*6, yu*1)
h9 = pygame.Rect(xu*13, yu*9, xu*8, yu*1)

horizWalls = [h1,h2,h3,h4,h5,h6,h7,h8,h9]

#initialize vertical walls
v1 = pygame.Rect(xu*6, yu*1, xu*1, yu*2)
v2 = pygame.Rect(xu*10, yu*1, xu*1, yu*2)
v3 = pygame.Rect(xu*14, yu*1, xu*1, yu*4)
v4 = pygame.Rect(xu*11, yu*7, xu*1, yu*3)
v5 = pygame.Rect(xu*8, yu*10, xu*1, yu*2)
v6 = pygame.Rect(xu*5, yu*12, xu*1, yu*4)
v7 = pygame.Rect(xu*14, yu*12, xu*1, yu*4)

vertWalls = [v1,v2,v3,v4,v5,v6,v7]

#draw the border
def drawBorders():  
    for wall in borderWalls:
        pygame.draw.rect(surface,BLACK,wall,0)

#draw the horizontal rectangles
def drawHorizontalRects():
    for wall in horizWalls:
        pygame.draw.rect(surface,BLACK,wall,0)

#draw the vertical rectangles  
def drawVerticalRects():
    for wall in vertWalls:
        pygame.draw.rect(surface,BLACK,wall,0)
        
#check collisions between both the player and gems inputted
def collidesWithWall(rectangle):
        for wall in borderWalls:     #if a rectangle collides with a border wall
            if rectangle.colliderect(wall):
                return True
        for wall in vertWalls:      #if a rectangle collides with a vertical wall
            if rectangle.colliderect(wall):
                return True
        for wall in horizWalls:     #if a rectangle collides with a horizontal wall
            if rectangle.colliderect(wall):
                return True
        return False

#place gems in different random locations
def placeGems():
    blueGemList = []
    greenGemList = []
    orangeGemList = []
    while len(blueGemList)<5:   #need 5 random blue gems inputted in maze
        blueGem = pygame.Rect(random.randint(0,w-20),random.randint(0,h-20),32,32)  #generate random location
        if collidesWithWall(blueGem) == False:   #if the random gem is not colliding with a wall
            blueGemList.append(blueGem)
        else:
            None
    
    #while len(orangeGemList)<2:   #need 2 random orange gems inputted in maze
        #orangeGem = pygame.Rect(random.randint(0,w-20),random.randint(0,h-20),32,32)  #generate random location
       # if collidesWithWall(orangeGem) == False:   #if the random gem is not colliding with a wall
         #   orangeGemList.append(orangeGem)
       # else:
         #   None    
            
   # while len(greenGemList)<3:   #need 3 random green gems inputted in maze
     #   greenGem = pygame.Rect(random.randint(0,w-20),random.randint(0,h-20),32,32)  #generate random location
      #  if collidesWithWall(greenGem) == False:   #if the random gem is not colliding with a wall
      #      greenGemList.append(greenGem)
      #  else:
         #   None
            
    return blueGemList, greenGemList,orangeGemList

#draw gems
def drawGems(blueGemList, greenGemList, orangeGemList):
    for gemsRect in blueGemList:
        surface.blit(blueGemStretched, gemsRect)
    #for gemsRect in greenGemList:
       # surface.blit(greenGemStretched, gemsRect)
   # for gemsRect in orangeGemList:
        #surface.blit(orangeGemStretched, gemsRect)

#draw the entire maze   
def drawMaze(blueGemList,greenGemList,orangeGemList):
    drawBorders()
    drawHorizontalRects()
    drawVerticalRects()
    drawGems(blueGemList, greenGemList, orangeGemList)
    pygame.draw.rect(surface, BLACK, e1)

#move the player based on single and continuous key presses    
def movePlayerOne(keys,speed1):
        if keys[pygame.K_LEFT] and collidesWithWall(playerOneRect) == False:  #if the left key is pressed and player is not colliding with any walls
            playerOneRect.left -= speed1
        if keys[pygame.K_LEFT] and collidesWithWall(playerOneRect) == True:
            playerOneRect.left += speed1
            
        if keys[pygame.K_RIGHT] and collidesWithWall(playerOneRect) == False:  #if the right key is pressed and player is not colliding with any walls
            playerOneRect.left += speed1
        if keys[pygame.K_RIGHT] and collidesWithWall(playerOneRect) == True:
            playerOneRect.left -= speed1
            
        if keys[pygame.K_UP] and collidesWithWall(playerOneRect) == False:     #if the up key is pressed and player is not colliding with any walls
            playerOneRect.top -= speed1
        if keys[pygame.K_UP] and collidesWithWall(playerOneRect) == True:
            playerOneRect.top += speed1
        
        if keys[pygame.K_DOWN] and collidesWithWall(playerOneRect) == False:   #if the down key is pressed and player is not colliding with any walls
            playerOneRect.top += speed1
        if keys[pygame.K_DOWN] and collidesWithWall(playerOneRect) == True:
            playerOneRect.top -= speed1
        
#move the player based on single and continuous key presses        
def movePlayerTwo(keys,speed2):
        if keys[pygame.K_a] and collidesWithWall(playerTwoRect) == False:  #if the left key is pressed and player is not colliding with any walls
            playerTwoRect.left -= speed2
        if keys[pygame.K_a] and collidesWithWall(playerTwoRect) == True:
            playerTwoRect.left += speed2
            
        if keys[pygame.K_d] and collidesWithWall(playerTwoRect) == False:  #if the right key is pressed and player is not colliding with any walls
            playerTwoRect.left += speed2
        if keys[pygame.K_d] and collidesWithWall(playerTwoRect) == True:
            playerTwoRect.left -= speed2
            
        if keys[pygame.K_w] and collidesWithWall(playerTwoRect) == False:     #if the up key is pressed and player is not colliding with any walls
            playerTwoRect.top -= speed2
        if keys[pygame.K_w] and collidesWithWall(playerTwoRect) == True:
            playerTwoRect.top += speed2
            
        if keys[pygame.K_s] and collidesWithWall(playerTwoRect) == False:   #if the down key is pressed and player is not colliding with any walls
            playerTwoRect.top += speed2
        if keys[pygame.K_s] and collidesWithWall(playerTwoRect) == True:
            playerTwoRect.top -= speed2           
        
#detect any gems collected throughout the maze      
def collectGems(blueGemList, greenGemList, orangeGemList, speed1, speed2, playerOnePowerUp, playerTwoPowerUp, playerOnePowerUpTime, playerTwoPowerUpTime, seconds):    
    for gemRect in blueGemList:
        if gemRect.colliderect(playerOneRect) and playerOnePowerUp == False:
            playerOnePowerUp = True
            blueGemList.remove(gemRect)#remove from map
            blueCollectSound.play()#play happy sound
            speed1 +=1
            playerOnePowerUpTime = seconds
        if gemRect.colliderect(playerTwoRect) and playerTwoPowerUp == False:  #if player collects the gems
            playerTwoPowerUp = True
            blueGemList.remove(gemRect)#remove from map
            blueCollectSound.play()#play happy sound            
            speed2+=1
            playerTwoPowerUpTime = seconds
            
    for gemRect in greenGemList:
        if gemRect.colliderect(playerOneRect) and playerOnePowerUp == False:
            playerOnePowerUpTime = seconds            
            playerOnePowerUp = True
            greenGemList.remove(gemRect)
            greenCollectSound.play()
            speed1 +=2
            playerOnePowerUpTime = seconds
        if gemRect.colliderect(playerTwoRect) and playerTwoPowerUp == False:
            playerTwoPowerUp = True            
            greenGemList.remove(gemRect)
            greenCollectSound.play()
            speed2 +=2
            playerTwoPowerUpTime = seconds            
            
    for gemRect in orangeGemList:
        if gemRect.colliderect(playerOneRect) and playerOnePowerUp == False:
            playerOnePowerUp = True            
            orangeGemList.remove(gemRect)
            orangeCollectSound.play()
            speed1 +=3
            playerOnePowerUpTime = seconds   
        if gemRect.colliderect(playerTwoRect) and playerOnePowerUp == False:
            playerTwoPowerUp = True            
            orangeGemList.remove(gemRect)
            orangeCollectSound.play()
            speed2 +=3
            playerTwoPowerUpTime = seconds            
            
    return blueGemList, greenGemList, orangeGemList, speed1, speed2, playerOnePowerUp, playerTwoPowerUp, playerOnePowerUpTime, playerTwoPowerUpTime

def showMessage(words, size,x,y, color,bg = None):     #code for the properties of the message blited on screen
    font = pygame.font.SysFont("Consolas", size, True, False)
    text = font.render(words, True, color,bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)  #needs = sign
    return  text, textBounds #returns image of text and its bounding rectangle needed for collision detection

#handles drawing the entire interface and delves into the text and bounds
def drawScreen(blueGemList, greenGemList, orangeGemList, gameOver, seconds,playerOneLives, playerTwoLives, p1, p2):
    drawMaze(blueGemList, greenGemList,orangeGemList)   #draws maze entirely
    surface.blit(p1,playerOneRect)
    surface.blit(p2,playerTwoRect)
    
    timeText, timeBounds = showMessage(str(10-seconds), 20, xu*.5,yu *.5, RED)   #gets text and rectangle bounds for timer
    surface.blit(timeText, timeBounds)      #display timer
    
    playerOneLivesText, playerOneLivesBounds = showMessage(str(playerOneLives), 20, xu*.5,h-yu*.5, RED)
    surface.blit(playerOneLivesText,playerOneLivesBounds)
    
    playerTwoLivesText, playerTwoLivesBounds = showMessage(str(playerTwoLives), 20, xu*18, h-yu*.5, RED)
    surface.blit(playerTwoLivesText,playerTwoLivesBounds)
    
    if gameOver == "player1win":   #if player1 wins
        winText, winBounds = showMessage("Player 1 wins! Press enter to play again.", 25,w/2, h/2, RED)  #get text and rectangle bounds for winner message
        surface.blit(winText,winBounds)   #display player1 wins message
    
    if gameOver == "player2win":   #if player2 wins
        loseText, loseBounds = showMessage("Player 2 wins!  Press enter to play again.", 25,w/2, h/2, RED)  #get text and rectangle bounds for loser message
        surface.blit(loseText,loseBounds)  #display player2 wins message
        
    #put other draw code here

#---------------------------------------Main Programming Loop------------------------------------
        
def main():
    blueGemList, greenGemList, orangeGemList = placeGems()
    gameOver = ""
    gameInPlay = True
    seconds = 0
    userScore = 0
    speedOne = 1
    speedTwo = 1
    playerOnePowerUp = False
    playerTwoPowerUp = False
    playerOnePowerUpTime = 0
    playerTwoPowerUpTime = 0
    whoIt = 1
    playerOneLives = 3
    playerTwoLives = 3
    
    while(True):
        if gameInPlay == True:   #if the game is in play
            keys = pygame.key.get_pressed()
            movePlayerOne(keys,speedOne)
            movePlayerTwo(keys,speedTwo)
            blueGemList, greenGemList,orangeGemList,speedOne,speedTwo, playerOnePowerUp, playerTwoPowerUp, playerOnePowerUpTime, playerTwoPowerUpTime = collectGems(blueGemList,greenGemList,orangeGemList,speedOne,speedTwo, playerOnePowerUp, playerTwoPowerUp, playerOnePowerUpTime, playerTwoPowerUpTime,seconds)
                
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:  #subtract second for each second
                seconds +=1             
            if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
                
        #game logic goes here            
        if seconds >= playerOnePowerUpTime + 10:    #if time is up for player one's power up
            playerOnePowerUp = False                #turn off player one's power up
            speedOne = 1                            #revert player one's speed back to 1
            playerOnePowerUpTime = seconds          #revert player one's power up timer
                    
        if seconds >= playerTwoPowerUpTime + 10:    #if time is up for player two's power up
            playerTwoPowerUp = False                #turn off player two's power up
            speedTwo = 1                            #revert player two's speed back to 1
            playerTwoPowerUpTime = seconds          #revert player two's power up timer           
        
        if playerOneRect.colliderect(playerTwoRect):            
            if whoIt == 1:
                blueGemList, greenGemList, orangeGemList = placeGems()
                playerOneRect.left = xu*1
                playerOneRect.bottom = yu*15
                playerTwoRect.left = xu*15
                playerTwoRect.bottom = yu*2
                
                playerOnePowerUp = False
                speedOne = 1
                playerOnePowerUpTime = seconds
                
                playerTwoPowerUp = False
                speedTwo = 1
                playerTwoPowerUpTime = seconds                  
                playerTwoLives-=1
                if(playerTwoLives <= 0):
                    gameInPlay = False  
                    gameOver = "player1win"
                
                playerTwoPowerUp = False                #turn off player two's power up
                speedTwo = 1                            #revert player two's speed back to 1
                playerTwoPowerUpTime = seconds          #revert player two's power up timer                  
                whoIt = 2
                seconds = 0                
                
        if playerOneRect.colliderect(playerTwoRect):                            
            if whoIt == 2:         #if player 2 is it
                blueGemList, greenGemList, orangeGemList = placeGems()
                playerOneRect.left = xu*1
                playerOneRect.bottom = yu*15
                playerTwoRect.left = xu*15
                playerTwoRect.bottom = yu*2

                playerOnePowerUp = False     #turn off player one power up
                speedOne = 1                 #revert player one's speed back
                playerOnePowerUpTime = seconds     #reset power up time
                
                playerTwoPowerUp = False     #urn off player two power up
                speedTwo = 1                 #revert player two's speed back
                playerTwoPowerUpTime = seconds      #reset power up time
                
                playerOneLives-=1
                if(playerOneLives <= 0):
                    gameInPlay = False
                    gameOver = "player2win"
                
                playerOnePowerUp = False                #turn off player one's power up
                speedOne = 1                            #revert player one's speed back to 1
                playerOnePowerUpTime = seconds          #revert player one's power up timer                
                whoIt = 1
                seconds = 0
                
        if seconds >= 10:
            blueGemList, greenGemList, orangeGemList = placeGems()
            playerOneRect.left = xu*1
            playerOneRect.bottom = yu*15
            playerTwoRect.left = xu*15
            playerTwoRect.bottom = yu*2
        
            playerOnePowerUp = False     #turn off player one power up
            speedOne = 1                 #revert player one's speed back
            playerOnePowerUpTime = seconds     #reset power up time
        
            playerTwoPowerUp = False     #urn off player two power up
            speedTwo = 1                 #revert player two's speed back
            playerTwoPowerUpTime = seconds      #reset power up time
        
            playerOnePowerUp = False                #turn off player one's power up
            speedOne = 1                            #revert player one's speed back to 1
            playerOnePowerUpTime = seconds          #revert player one's power up timer 
            if whoIt == 2: 
                whoIt = 1
            elif whoIt == 1:
                whoIt = 2
            seconds = 0            
        
        if gameInPlay == False:  #if the game is over
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  #if the player wants to play again press enter
                blueGemList, greenGemList, orangeGemList = placeGems()
                gameOver = ""
                gameInPlay = True
                seconds = 0
                pygame.time.set_timer(pygame.USEREVENT, 1000)
                playerOneRect.left = xu*1
                playerOneRect.bottom = yu*16
                playerOneLives = 3;
                playerTwoLives = 3;
                speedOne = 1
                speedTwo = 1                
        
        #set background color
        surface.fill(WHITE)
            
        #draw code goes here
        if whoIt == 1:
            drawScreen(blueGemList, greenGemList, orangeGemList, gameOver, seconds, playerOneLives,playerTwoLives, playerOneShrinkedIt, playerTwoShrinked)
        
        if whoIt == 2:
            drawScreen(blueGemList, greenGemList, orangeGemList, gameOver, seconds, playerOneLives,playerTwoLives, playerOneShrinked, playerTwoShrinkedIt)
        
        #update screen
        pygame.display.update()   
        
main()
