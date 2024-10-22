import pygame
from Constants import *
pygame.init()

from random import randint

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tanks")

done = False
FPS = 240


Coordinates1 = [100, 100]
Coordinates2 = [600, 300]
STEP = 5
projectile1 = None
projectile2 = None

clock = pygame.time.Clock() 

def hit(projectile, tank):
    if tank[0]<projectile[0]< tank[0] +20 and tank[1]<projectile[1]< tank[1] +30:
        return True


while not done:


    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
            print(event)
            key = event.dict.get("key")
            match key:
                case 119:
                    Coordinates1[1] -= STEP
                case 100:
                    Coordinates1[0] += STEP
                case 115:
                    Coordinates1[1] += STEP
                case 97:
                    Coordinates1[0] -= STEP
                case 32:
                    projectile1 = [Coordinates1[0]+30, Coordinates1[1]+12]


                case 1073741906:
                    Coordinates2[1] -= STEP
                case 1073741903:
                    Coordinates2[0] += STEP
                case 1073741905:
                    Coordinates2[1] += STEP
                case 1073741904:
                    Coordinates2[0] -= STEP






    gameDisplay.fill(White)

    pygame.draw.rect(gameDisplay, Gray, pygame.Rect(Coordinates1[0], Coordinates1[1], 20, 30), width=0)
    pygame.draw.rect(gameDisplay, Black, pygame.Rect(Coordinates1[0]+20, Coordinates1[1]+12, 10, 5), width=0)
    
    if projectile1:
        projectile1[0] += 5
        pygame.draw.circle(gameDisplay, Red, projectile1, 3, width=0)
        if hit(projectile1, Coordinates2):
            print("win1")
            break


        if projectile1[0] > 800:
            projectile1 = None
        


    Coordinates2[1] += randint(-5, 5)
    pygame.draw.rect(gameDisplay, Gray, pygame.Rect(Coordinates2[0], Coordinates2[1], 20, 30), width=0)
    pygame.draw.rect(gameDisplay, Black, pygame.Rect(Coordinates2[0]-10, Coordinates2[1]+12, 10, 5), width=0)
    
    if projectile2:
        projectile2[0] -= 5
        pygame.draw.circle(gameDisplay, Red, projectile2, 3, width=0)
        if projectile2[0] > 800:
            projectile2 = None

    pygame.display.update()
    clock.tick(FPS)