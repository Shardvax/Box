#We have to import pygame to use it
import pygame

import random
#All pygame programs must init before using its library
pygame.init()

#Set variables for our window size
windowwidth = 1500
windowheight = 1000
#Create our window
win = pygame.display.set_mode((windowwidth,windowheight))
white = (255, 255, 255)
blue = (0,0,205)
#deepskyblue (0,191,255)
#lightblue (135,206,250)
#blue (0, 0, 255)
#mediumblue (0,0,205)
black = (0, 0, 0)
yellow = (255, 255, 0)
#Set our window's title bar
class Player:
    IsBlue = False
    IsWhite = False
    IsWASD = False
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 100
        self.height = 100
        #We need to track the player's velocity between frames for its y coordinate so that jumping will work.
        #If we wanted to acceleration / deceleration for our left/right movement we could also track x velocity.
        self.vely = 0
        self.gravity = 2.5
        self.jumping = False
        self.jumppower = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.coincount = 0

    def tick(self):
        # INPUT
        if not self.IsWASD:
            if keys[pygame.K_LEFT]:
                self.x -= 30
            if keys[pygame.K_RIGHT]:
                self.x += 30
            if keys[pygame.K_UP] and self.jumping == False:
                self.vely = -self.jumppower
                self.jumping = True

        if self.IsWASD:
            if keys[pygame.K_a]:
                self.x -= 30
            if keys[pygame.K_d]:
                self.x += 30
            if keys[pygame.K_w] and self.jumping == False:
                self.vely = -self.jumppower
                self.jumping = True

        self.vely += self.gravity
        self.y += self.vely

        if self.x > windowwidth - self.width:
            self.x = windowwidth - self.width
        if self.x < 0:
            self.x = 0
        if self.y > windowheight - self.height:
            self.y = windowheight - self.height
            self.vely = 0
            self.jumping = False
        if self.y < 0:
            self.y = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.IsBlue:
            pygame.draw.rect(win, blue, self.rect)
        if self.IsWhite:
            pygame.draw.rect(win, white, self.rect)

class Player2:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 100
        self.height = 100
        #We need to track the player's velocity between frames for its y coordinate so that jumping will work.
        #If we wanted to acceleration / deceleration for our left/right movement we could also track x velocity.
        self.vely = 0
        self.gravity = 2.5
        self.jumping = False
        self.jumppower = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.coincount = 0

    def tick(self):
        # INPUT

        if keys[pygame.K_a]:
            self.x -= 30
        if keys[pygame.K_d]:
            self.x += 30
        if keys[pygame.K_w] and self.jumping == False:
            self.vely = -self.jumppower
            self.jumping = True

        self.vely += self.gravity
        self.y += self.vely

        if self.x > windowwidth - self.width:
            self.x = windowwidth - self.width
        if self.x < 0:
            self.x = 0
        if self.y > windowheight - self.height:
            self.y = windowheight - self.height
            self.vely = 0
            self.jumping = False
        if self.y < 0:
            self.y = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, blue, self.rect)

class Pickup:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 100
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def tick(self):
        if self.rect.colliderect(player.rect) == True:
            player.coincount += 10
            player2.coincount += 10
            print("Player 1: $" + str(player.coincount))
            print("Player 2: $" + str(player2.coincount))
            overlapping = True
            while overlapping == True:
                self.x = random.randint(0, windowwidth - coin.width)
                self.y = random.randint(windowheight // 2 - self.height // 2, windowheight - coin.height)
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                if self.rect.colliderect(player.rect and player2.rect) == False:
                    overlapping = False
        if self.rect.colliderect(player2.rect) == True:
            player2.coincount += 10
            print("Player 2: $" + str(player2.coincount))
            overlapping = True
            while overlapping == True:
                self.x = random.randint(0, windowwidth - coin.width)
                self.y = random.randint(windowheight // 2 - self.height // 2, windowheight - coin.height)
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                if self.rect.colliderect(player.rect and player2.rect) == False:
                    overlapping = False

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.ellipse(win, yellow, self.rect, 15)
#Right before our game loop begins, we will contruct our player.
#We can do this by calling Player() - this will run the __init__(self) function that we just wrote to create a player.

player = Player()
coin = Pickup()
player.IsWhite = True
player2 = Player2()

pygame.display.set_caption("Python Platformer")
#Define our run variable, when this becomes False the window will close and the program will end
run = True
#Run our core game loop: right now this does nothing except keep the window open
while run:
     pygame.time.delay(22)

     for event in pygame.event.get():
          if event.type == pygame.QUIT:
                run = False

     keys = pygame.key.get_pressed()
     win.fill(black)
     player.tick()
     player2.tick()
     coin.tick()
     while player.coincount == 500:
         run = False
         print("Player 1 wins!")
         break
     while player2.coincount == 500:
         run = False
         print("Player 2 wins!")
         break
# This is where most of our game code would go!

#Update the pygame display with whatever we drew on the screen this time through the loop
#If you forget this line of code you'll only ever see a black window
     pygame.display.update()
print("Game Over")