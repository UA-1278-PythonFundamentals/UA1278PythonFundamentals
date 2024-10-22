import pygame
from Constants import *
pygame.init()


gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Tanks")

done = False
FPS = 60
POINTS = []

clock = pygame.time.Clock() 
font = pygame.font.SysFont('Calibri', 25, True, False)


while not done:


    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
            print(event)
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
            print(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            key = event.dict.get("button")
            print("User pressed a mouse button", event)
            if key == 1:
                print(event.dict.get("pos"))
                POINTS.append(event.dict.get("pos"))
            elif key == 3 and POINTS:
                print(f"remove point {POINTS.pop()}")
            print(POINTS)



    gameDisplay.fill(White)

    if len(POINTS) >= 3:
        pygame.draw.polygon(gameDisplay, Colors[len(POINTS)%len(Colors)], POINTS, width=0)

    for i, point in enumerate(POINTS):
        text = font.render(f"{i}-{point}",True, Black)
        gameDisplay.blit(text, point)

    pygame.display.update()
    clock.tick(FPS)