import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((900, 500))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
done = False
FPS = 60
COLORS = (128, 128, 0)
WHITE = (255, 255, 255)
Coordinates = [100, 100]
STEP = 5

while not done:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            print("User asket to quit")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
            print(event)
            key = event.dict.get("key")
            match key:
                case 1073741904:
                   Coordinates[0] -= STEP
                case 1073741903:
                    Coordinates[0] += STEP
                case 1073741906:
                    Coordinates[1] -= STEP
                case 1073741905:
                    Coordinates[1] += STEP
      


    gameDisplay.fill(WHITE)
    pygame.draw.rect(gameDisplay, COLORS, pygame.Rect(Coordinates[0], Coordinates[1], 50, 50), width=0)


    pygame.display.update()
    clock.tick(FPS)