import pygame
import random

pygame.init()

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("guess a number")
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 18, True)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
FPS = 60
DONE = False

guested_number = random.randint(1, 100)
print(guested_number)
input_number = ""
attempt = 0

main_text = font.render("Enter your number, than press ENTER", True, BLACK)
main_text_rect = main_text.get_rect()
main_text_rect.center = (400, 100)

not_numeric_error = False
greater_100_error = False
start_with_0_error = False

congratulation = False

while not DONE:
    game_display.fill(WHITE)

    if attempt > 10:
        end_game_text = font.render("you've wasted all your attempts", True, BLACK)
        end_game_rect = end_game_text.get_rect()
        end_game_rect.center = (400, 200)
        game_display.blit(end_game_text, end_game_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DONE = True

    elif congratulation:
        congratulation_text = font.render(f"You guessed the number!", True, GREEN)
        congratulation_rect = congratulation_text.get_rect()
        congratulation_rect.center = (400, 200)
        game_display.blit(congratulation_text, congratulation_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DONE = True

    else:
        game_display.blit(main_text, main_text_rect)

        number_text = font.render(f"Your number: {input_number}", True, BLACK)
        number_text_rect = number_text.get_rect()
        number_text_rect.center = (400, 130)
        game_display.blit(number_text, number_text_rect)

        attempt_text = font.render(f"Your attempt: {attempt}", True, BLACK)
        attempt_text_rect = attempt_text.get_rect()
        attempt_text_rect.center = (400, 150)
        game_display.blit(attempt_text, attempt_text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DONE = True

            if event.type == pygame.TEXTINPUT:
                num = event.dict.get("text")
                if num == "0" and len(input_number) == 0:
                    start_with_0_error_text = font.render(f"num can not start with 0!",
                                                          True, RED)
                    start_with_0_error_rect = start_with_0_error_text.get_rect()
                    start_with_0_error_rect.center = (400, 200)

                    greater_100_error = False
                    not_numeric_error = False

                    start_with_0_error = True
                elif not num.isnumeric():
                    invalid_input_text = font.render(f"{num} is not numeric!",
                                                     True, RED)
                    invalid_input_rect = invalid_input_text.get_rect()
                    invalid_input_rect.center = (400, 200)

                    greater_100_error = False
                    start_with_0_error = False

                    not_numeric_error = True
                else:
                    input_number += num
                    if int(input_number) > 100:
                        greater_100_error = True
                        greater_100_text = font.render(f"{input_number} is greater than 100! try again",
                                                       True, RED)
                        greater_100_rect = greater_100_text.get_rect()
                        greater_100_rect.center = (400, 200)
                        input_number = ""
                    else:
                        greater_100_error = False
                        not_numeric_error = False
                        start_with_0_error = False

            if event.type == pygame.KEYDOWN:
                if event.dict.get("key") == 13:
                    if not input_number.isnumeric() or input_number == "0":
                        continue
                    input_number = int(input_number)
                    if input_number != guested_number:
                        attempt += 1
                        input_number = ""
                    else:
                        congratulation = True
                        input_number = ""

        if not_numeric_error:
            game_display.blit(invalid_input_text, invalid_input_rect)
        if greater_100_error:
            game_display.blit(greater_100_text, greater_100_rect)
        if start_with_0_error:
            game_display.blit(start_with_0_error_text, start_with_0_error_rect)

    pygame.display.update()
    clock.tick(FPS)
