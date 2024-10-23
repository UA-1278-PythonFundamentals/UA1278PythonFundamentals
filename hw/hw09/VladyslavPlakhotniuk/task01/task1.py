import pygame
import random
import sys

pygame.init()

window = pygame.display.set_mode((600, 200))
pygame.display.set_caption("Угадай число від 1 до 100")

WHITE = (245, 245, 245)
BLACK = (30, 30, 30)
GREEN = (144, 238, 144)
RED = (255, 105, 97)

font = pygame.font.Font(None, 56)

zagadka = random.randint(1, 100)
max_sprob = 10
sproby = 0
vhid_chysla = ""
result_message = ""

running = True
while running:
    window.fill(WHITE)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if vhid_chysla.isdigit():
                    sproby += 1
                    user_guess = int(vhid_chysla)

                    if user_guess == zagadka:
                        result_message = "Вітаємо! Ти вгадав число!"
                        running = False
                    elif user_guess < zagadka:
                        result_message = "Загадане число більше."
                    else:
                        result_message = "Загадане число менше."

                    vhid_chysla = ""
                if sproby >= max_sprob:
                    result_message = f"Спроби закінчились! Число було: {zagadka}."
                    running = False

            elif event.key == pygame.K_BACKSPACE:
                vhid_chysla = vhid_chysla[:-1]
            else:
                vhid_chysla += event.unicode

    prompt = font.render("Введи число від 1 до 100:", True, BLACK)
    window.blit(prompt, (30, 30))

    input_text = font.render(vhid_chysla, True, GREEN)
    window.blit(input_text, (30, 60))

    attempts_text = font.render(f"Спроба: {sproby}/{max_sprob}", True, BLACK)
    window.blit(attempts_text, (20, 100))

    result_text = font.render(result_message, True, RED)
    window.blit(result_text, (20, 140))

    pygame.display.flip()

pygame.quit()
