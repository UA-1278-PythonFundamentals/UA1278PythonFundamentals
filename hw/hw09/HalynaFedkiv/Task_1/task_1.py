"""Write a game script that randomly generates a number from a range of
1 to 100 and asks the user to guess that number in 10 tries.
The program reads the numbers entered by the user and prompts the user
whether the guessed number is greater or less than the number entered by the
user. The game must continue until the user has used 10 attempts and guessed
the number. If the user guessed the number, the program prints a
congratulatory message, and if 10 attempts have been exhausted and the user
did not have time to guess the number, then the corresponding message is
displayed."""

import constants
import pygame
from random import randint


pygame.init()

clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Guess the number')
icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)
surface_img = pygame.image.load('qm.jpg')
gameDisplay.blit(surface_img, (0, 0))


done = False
FPS = 60
number = randint(1, 100)
list_of_guesses = []

capital_font = pygame.font.SysFont('Calibri', 26, True, False)
small_font = pygame.font.SysFont('Calibri', 20, False, False)

user_text = ''
input_rect = pygame.Rect(150, 190, 20, 40)


def render_text(text, font, color, surface, x, y):
    text_surface = font.render(text, False, color)
    surface.blit(text_surface, (x, y))


def get_guess():
    list_of_guesses.append(user_text)
    return user_text


def check_guess(guess, number):
    if len(list_of_guesses) == 10:
        gameDisplay.fill(constants.Black)
        render_text(f'You ran out of tries. The number was {number}.', capital_font, constants.White,
                    gameDisplay, 135, 220)
        render_text(f'Game over!', capital_font, constants.White, gameDisplay, 300, 280)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
    elif int(guess) == number:
        gameDisplay.fill(constants.Green)
        render_text(f'Well done!', capital_font, constants.White, gameDisplay, 285, 180)
        render_text(f'You have guessed my number in {len(list_of_guesses)} {"tries" if len(list_of_guesses) > 1 else "try"}!',
                    capital_font, constants.White, gameDisplay, 105, 240)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
    elif int(guess) < number:
        gameDisplay.blit(surface_img, (0, 0))
        render_text(f'Your number is less than mine. Try again!', capital_font, constants.Navy_Blue, gameDisplay, 20, 350)
        pygame.display.flip()
    else:
        gameDisplay.blit(surface_img, (0, 0))
        render_text(f'Your number is greater than mine. Try again!', capital_font, constants.Navy_Blue, gameDisplay, 20, 350)
        pygame.display.flip()


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                my_guess = get_guess()
                check_guess(my_guess, number)
            else:
                user_text += event.unicode

    render_text("I'm thinking of a random number between 1 and 100.", capital_font, constants.Black, gameDisplay, 85, 50)
    render_text("Guess what number I am thinking of.", capital_font, constants.Black, gameDisplay, 165, 90)
    render_text("Your guess: ", small_font, constants.Black, gameDisplay, 20, 200)
    render_text("You've already tried these ones: " + ', '.join(map(str, list_of_guesses)), small_font, constants.Black, gameDisplay, 20, 250)

    pygame.draw.rect(gameDisplay, constants.White, input_rect)
    text_input = capital_font.render(user_text, True, constants.Navy_Blue)

    gameDisplay.blit(text_input, (input_rect.x + 5, input_rect.y + 5))

    # set width of textfield so that text cannot get outside of user's text input
    input_rect.w = max(80, text_input.get_width() + 10)

    pygame.display.update()
    clock.tick(FPS)
