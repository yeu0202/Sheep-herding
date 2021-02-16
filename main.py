# 1 - Import library
import pygame
from pygame.locals import *
import random
import time

# 2 - Initialize the game
pygame.init()
width, height = 1280, 960
screen = pygame.display.set_mode((width, height))

# 3 - Load images
playerImg = pygame.image.load("resources/Ismark.png").convert_alpha()
playerImg = pygame.transform.scale(playerImg, (100, 100))
backgroundImg = pygame.image.load("resources/openField.jpg")
backgroundImg = pygame.transform.scale(backgroundImg, (width, height))
houseImg = pygame.image.load("resources/house.png").convert_alpha()
houseImg = pygame.transform.scale(houseImg, (100, 100))
youWinImg = pygame.image.load("resources/youWin.png").convert_alpha()
youWinImg = pygame.transform.scale(youWinImg, (400, 400))

# create sheep
sheepImg = pygame.image.load("resources/sheep.png").convert_alpha()
sheepImg = pygame.transform.scale(sheepImg, (100, 100))
happySheepImg = pygame.image.load("resources/happySheep.png").convert_alpha()
happySheepImg = pygame.transform.scale(happySheepImg, (100, 100))
sheepPositions = []
for i in range(5):
    sheepPositions.append([random.randint(50, width-50), random.randint(50, height-50)])
print(sheepPositions)
safeSheep = 0
wonGame = False
timeCounter = 0

housePosition = [300, 400]
scareDistance = 150


def findDistance(object1, object2):
    return (((object1[0] - object2[0])**2) + ((object1[1] - object2[1])**2)) ** (1/2)

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


# 4 - keep looping through
while True:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(backgroundImg, (0, 0))
    cursorPosition = pygame.mouse.get_pos()
    screen.blit(playerImg, (cursorPosition[0]-50, cursorPosition[1]-50))

    screen.blit(houseImg, (housePosition[0]-50, housePosition[1]-50))  # house position

    safeSheep = 0
    for sheep in sheepPositions:
        if findDistance(cursorPosition, sheep) < scareDistance:
            sheep[0] = sheep[0] - (cursorPosition[0] - sheep[0])/20
            sheep[1] = sheep[1] - (cursorPosition[1] - sheep[1])/20
        if random.randint(0, 20) == 0 and not wonGame:
            sheep[0] = sheep[0] + random.randint(-3, 3)
            sheep[1] = sheep[1] + random.randint(-3, 3)
        sheep[0] = clamp(sheep[0], 50, width-50)
        sheep[1] = clamp(sheep[1], 50, height - 50)

        if findDistance((housePosition[0], housePosition[1]), sheep) < 100:
            screen.blit(happySheepImg, (sheep[0] - 50, sheep[1] - 50))
            safeSheep += 1
        else:
            screen.blit(sheepImg, (sheep[0] - 50, sheep[1] - 50))

    if safeSheep == len(sheepPositions):
        screen.blit(youWinImg, (width/2-200, height/2-200))
        wonGame = True

    if wonGame:
        timeCounter += 1
    if timeCounter > 1200:
        pygame.quit()
        exit(1)

    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)