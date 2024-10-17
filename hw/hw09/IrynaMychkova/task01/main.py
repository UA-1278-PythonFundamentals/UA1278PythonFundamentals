import time
import pygame
import random

WHITE = (255, 255, 255)
NAVYBLUE = (60, 60, 100)
DARKNAVYBLUE = (0, 0, 100)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

greeting_texts = [
    "Hi there! Welcome to the land of wizzards and dragons!", 
    "Only true Wizards can guess the number I'm thinking of!",
    "Are you the One? Try to guess the number.",
    "You have 10 attempts.",
    "Enter your number (1 .. 100) and press Return:",
]

pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
font = pygame.font.SysFont('Calibri', 25, True, False)

pygame.display.set_caption('My first game')
clock = pygame.time.Clock() 

def get_random_integer(a = 1 , b = 100) -> int:
    """
    This function generates a random integer in the range [a, b] (including a and b).
    """
    return random.randint(a, b)

def text_objects(text, font, color = NAVYBLUE):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, color = NAVYBLUE, y = DISPLAY_HEIGHT / 2, x = DISPLAY_WIDTH / 2, font_size = 25):
    font = pygame.font.SysFont('Calibri', font_size, True, False)
    TextSurf, TextRect = text_objects(text, font, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def display_message_block(texts: list, y = DISPLAY_HEIGHT / 2, alignment = 'center'):
    line_height = 45
    match alignment:
        case 'left':
            x = DISPLAY_WIDTH / 8 * 2
        case 'right':
            x = DISPLAY_WIDTH / 8 * 6
        case _:
            x = DISPLAY_WIDTH / 2  # Default to center if alignment is not 'left' or 'right'

    for i, text in enumerate(texts[::-1]):
        message_display(text, x = x, y = y + i * line_height)


def display_attempts(attempts: list, current_attempt: str):
    if current_attempt:
        message_display(current_attempt, y=DISPLAY_HEIGHT * 0.42)

    if len(attempts) > 5:
        display_message_block(attempts[-5:], DISPLAY_HEIGHT * 0.47, 'left')
        display_message_block(attempts[:-5], DISPLAY_HEIGHT * 0.47, 'right')
    else:
        display_message_block(attempts, DISPLAY_HEIGHT * 0.47, 'left')

def failed(reason):
    message_display(f"Sorry, you failed. {reason}", color = (255, 0, 0), y = DISPLAY_HEIGHT * 0.9)
    pygame.display.update()
    time.sleep(3)
    # Clear the event queue
    pygame.event.clear()
    game_loop()

def game_loop(done = False):
    print('Game loop started')
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    number_pressed = list()
    last_number = ''

    # -------- Main Program Loop -----------
    while not done:
        
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP: 
                if event.unicode and event.unicode.isdigit():
                    last_number += event.unicode
                elif event.key == pygame.K_RETURN and last_number:
                    number_pressed.append(last_number)
                    last_number = ''

                if last_number and int(last_number) > 100:
                    number_pressed.append('Wrong number')
                    last_number = ''

            if len(number_pressed) >= 10:
                failed("Got out of attempts")

        # --- Game logic should go here

        # --- Drawing code should go here
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        gameDisplay.fill(WHITE)

        display_message_block(greeting_texts[::-1], y = DISPLAY_HEIGHT * 0.05)

        # Draw numbers pressed:
        display_attempts(number_pressed, last_number)
      

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.update()
        # --- Limit to 60 frames per second
        clock.tick(30)

game_loop()
pygame.quit()
quit()
