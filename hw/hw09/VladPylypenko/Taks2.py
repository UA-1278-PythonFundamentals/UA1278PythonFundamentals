# Task 2.
# You need to change the code Rect_pygame.py
#  program so that the rectangle does not extend beyond
#  the program window.

import pygame

FPS = 60

WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500

COORD_X = 50
COORD_Y = 50
WIDTH_RECTANGLE = 40
HEIGHT_RECTANGLE = 60
DELTA_STEP = 5

WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 0, 255)

pygame.init()

gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
pygame.display.set_caption("My first game")

run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        COORD_X -= DELTA_STEP
    if keys[pygame.K_d]:
        COORD_X += DELTA_STEP
    if keys[pygame.K_w]:
        COORD_Y -= DELTA_STEP
    if keys[pygame.K_s]:
        COORD_Y += DELTA_STEP

    if COORD_X < 0:
        COORD_X = 0
    if COORD_X > WIDTH_DISPLAY - WIDTH_RECTANGLE:
        COORD_X = WIDTH_DISPLAY - WIDTH_RECTANGLE
    if COORD_Y < 0:
        COORD_Y = 0
    if COORD_Y > HEIGHT_DISPLAY - HEIGHT_RECTANGLE:
        COORD_Y = HEIGHT_DISPLAY - HEIGHT_RECTANGLE

    gameDisplay.fill(WHITE_COLOR)

    pygame.draw.rect(gameDisplay, BLUE_COLOR, [COORD_X,
                                               COORD_Y,
                                               WIDTH_RECTANGLE,
                                               HEIGHT_RECTANGLE])
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()