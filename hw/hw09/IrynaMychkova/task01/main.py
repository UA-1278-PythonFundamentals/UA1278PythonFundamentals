import time
import pygame
import random

# Constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
NAVYBLUE = (60, 60, 100)
DARKNAVYBLUE = (0, 0, 100)
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# Greeting texts
greeting_texts = [
    "Hi there! Welcome to the land of wizzards and dragons!", 
    "Only true Wizards can guess the number I'm thinking of!",
    "Are you the One? Try to guess the number.",
    "You have 10 attempts.",
    "Enter your number (1 .. 100) and press Return:",
]

# Initialize Pygame
pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('My first game')
clock = pygame.time.Clock()

def get_random_integer(a=1, b=100) -> int:
    """Generate a random integer in the range [a, b]."""
    return random.randint(a, b)

def text_objects(text, font, color=DARKNAVYBLUE):
    """Render text to a surface and return the surface and its rectangle."""
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, color=DARKNAVYBLUE, y=DISPLAY_HEIGHT / 2, x=DISPLAY_WIDTH / 2, font_size=25):
    """Display a message on the screen."""
    font = pygame.font.SysFont('Calibri', font_size, True, False)
    TextSurf, TextRect = text_objects(text, font, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def display_message_block(texts: list, y=DISPLAY_HEIGHT / 2, alignment='center'):
    """Display a block of messages on the screen."""
    line_height = 45
    x = {
        'left': DISPLAY_WIDTH / 8 * 2,
        'right': DISPLAY_WIDTH / 8 * 6
    }.get(alignment, DISPLAY_WIDTH / 2)  # Default to center

    for i, text in enumerate(texts[::-1]):
        message_display(text, x=x, y=y + i * line_height)

def display_attempts(attempts: list, current_attempt: str):
    """Display the attempts made by the player."""
    if current_attempt:
        message_display(current_attempt, y=DISPLAY_HEIGHT * 0.42)

    if len(attempts) > 5:
        display_message_block(attempts[-5:], DISPLAY_HEIGHT * 0.47, 'left')
        display_message_block(attempts[:-5], DISPLAY_HEIGHT * 0.47, 'right')
    else:
        display_message_block(attempts, DISPLAY_HEIGHT * 0.47, 'left')

def check_number(secret_number, number, game_over) -> str:
    """Check if the guessed number is correct."""
    if game_over:
        return ""
    print(f"Checking number {number}")
    if secret_number == number:
        succeed(str(secret_number))
        return ""
    elif secret_number > number:
        return "Nope. More"
    else: 
        return "Nope. Less"

def failed(reason):
    """Handle the failure case."""
    message_display(f"Try again. My number was {reason}", color=RED, y=DISPLAY_HEIGHT * 0.9)
    pygame.display.update()
    time.sleep(3)
    pygame.event.clear()
    game_loop()

def succeed(reason):
    """Handle the success case."""
    message_display(f"Well done {reason}", color=GREEN, y=DISPLAY_HEIGHT * 0.9)
    pygame.display.update()
    time.sleep(3)
    pygame.event.clear()
    game_loop()

def game_loop(done=False):
    """Main game loop."""
    secret_number = get_random_integer()
    print('Game loop started ' + str(secret_number))
    number_pressed = list()
    last_number = ''
    game_over = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP and not game_over:
                if event.unicode and event.unicode.isdigit():
                    last_number += event.unicode
                elif event.key == pygame.K_RETURN and last_number:
                    number_pressed.append(last_number)
                    last_number = ''

                if last_number and int(last_number) > 100:
                    number_pressed.append('Wrong number')
                    last_number = ''

                if len(number_pressed) >= 10:
                    game_over = True

        gameDisplay.fill(WHITE)
        display_message_block(greeting_texts[::-1], y=DISPLAY_HEIGHT * 0.05)
        display_attempts(number_pressed, last_number)
        
        if not game_over and number_pressed:
            message = check_number(secret_number, int(number_pressed[-1] or 0), game_over)
            if message:
                message_display(message, y=DISPLAY_HEIGHT * 0.9)
        elif game_over:
            failed(secret_number)
            done = True
        
        pygame.display.update()
        clock.tick(30)

game_loop()
pygame.quit()
quit()