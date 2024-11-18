# Task 1. Write a game script that randomly generates a number from a range of
# 1 to 100 and asks the user to guess that number in 10 tries.
# The program reads the numbers entered by the user and prompts the user
# whether the guessed number is greater or less than the number entered by the
# user. The game must continue until the user has used 10 attempts and guessed
# the number. If the user guessed the number, the program prints a
# congratulatory message, and if 10 attempts have been exhausted and the user
# did not have time to guess the number, then the corresponding message is
# displayed (to perform the task, you need to import the random module,
# and from it the randint() function)

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 420, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Number Guessing Game")

# Load fonts
title_font = pygame.font.SysFont('Arial', 24, bold=True)
normal_font = pygame.font.SysFont('Arial', 18)


# Game class
class NumberGuessingGame:
    def __init__(self):
        self.target_number = random.randint(1, 100)
        self.attempts = 10
        self.remaining_attempts = self.attempts
        self.success_attempt = None
        self.input_box = pygame.Rect(110, 150, 200, 32)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.active = False
        self.text = ''
        self.result_text = ''
        self.attempts_text = f"Remaining attempts: {self.remaining_attempts}"
        self.show_try_again = False  # Flag to show "Try Again" button
        self.cursor_visible = True  # Для видимості курсора
        self.cursor_timer = pygame.time.get_ticks()  # Таймер для курсора

    def draw(self):
        screen.fill(WHITE)

        # Draw title
        title_surface = title_font.render("Welcome to the Number Guessing Game!", True, BLUE)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 25))
        screen.blit(title_surface, title_rect)

        # Draw instructions
        instructions_surface = normal_font.render("Select a number between 1 and 100.", True, ORANGE)
        instructions_rect = instructions_surface.get_rect(center=(SCREEN_WIDTH // 2, 60))
        screen.blit(instructions_surface, instructions_rect)

        # Draw input box
        txt_surface = normal_font.render(self.text, True, self.color)
        width = max(200, txt_surface.get_width() + 10)
        self.input_box.w = width
        pygame.draw.rect(screen, self.color, self.input_box, 2)
        screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))

        # Draw result text
        result_surface = normal_font.render(self.result_text, True, RED)
        result_rect = result_surface.get_rect(center=(SCREEN_WIDTH // 2, 215))
        screen.blit(result_surface, result_rect)

        # Draw attempts text
        attempts_surface = normal_font.render(self.attempts_text, True, ORANGE)
        attempts_rect = attempts_surface.get_rect(center=(SCREEN_WIDTH // 2, 315))
        screen.blit(attempts_surface, attempts_rect)

        # Draw cursor
        if self.active and self.cursor_visible:
            cursor_x = self.input_box.x + 5 + txt_surface.get_width()  # Позиція курсора
            cursor_height = 20  # Висота курсора
            cursor_rect = pygame.Rect(cursor_x, self.input_box.y + 5, 2, cursor_height)  # Прямокутник курсора
            pygame.draw.rect(screen, BLACK, cursor_rect)

        # Draw Guess button
        guess_button_surface = normal_font.render("Guess", True, WHITE)
        guess_button_rect = pygame.Rect((SCREEN_WIDTH - 80) // 2, 250, 80, 30)
        pygame.draw.rect(screen, GREEN, guess_button_rect)
        guess_button_text_rect = guess_button_surface.get_rect(center=guess_button_rect.center)
        screen.blit(guess_button_surface, guess_button_text_rect)

        # Draw Try Again button if the game has ended
        if self.show_try_again:
            try_again_surface = normal_font.render("Try Again", True, WHITE)
            try_again_button_rect = pygame.Rect((SCREEN_WIDTH - 100) // 2, 360, 100, 30)
            pygame.draw.rect(screen, BLUE, try_again_button_rect)
            try_again_text_rect = try_again_surface.get_rect(center=try_again_button_rect.center)
            screen.blit(try_again_surface, try_again_text_rect)

        pygame.display.flip()

        return guess_button_rect, try_again_button_rect if self.show_try_again else None  # Return button rectangles

    def handle_guess(self):
        try:
            guess = int(self.text)
            self.text = ''  # Clear input field

            if guess < 1 or guess > 100:
                self.result_text = "Please enter a number between 1 and 100."
                return

            self.remaining_attempts -= 1

            if guess == self.target_number:
                self.success_attempt = self.attempts - self.remaining_attempts
                self.result_text = f"Congratulations! You guessed the number {self.target_number} in {self.success_attempt} attempts!"
                self.show_try_again = True  # Show Try Again button
            elif guess < self.target_number:
                self.result_text = "Your guess is too low. Try again."
            else:
                self.result_text = "Your guess is too high. Try again."

            if self.remaining_attempts == 0:
                self.result_text = f"Sorry, you've used all attempts. The correct number was {self.target_number}."
                self.show_try_again = True  # Show Try Again button

            self.attempts_text = f"Remaining attempts: {self.remaining_attempts}"

        except ValueError:
            self.result_text = "Please enter a valid integer."

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.remaining_attempts = self.attempts
        self.success_attempt = None
        self.text = ''
        self.result_text = ''
        self.attempts_text = f"Remaining attempts: {self.remaining_attempts}"
        self.show_try_again = False  # Hide Try Again button

    def update_cursor(self):
        if self.active and pygame.time.get_ticks() - self.cursor_timer > 500:  # 500 ms
            self.cursor_visible = not self.cursor_visible  # Toggle cursor visibility
            self.cursor_timer = pygame.time.get_ticks()  # Reset timer


# Create game instance
game = NumberGuessingGame()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            guess_button_rect, try_again_button_rect = game.draw()  # Draw and get button rectangles
            if game.input_box.collidepoint(event.pos):
                game.active = not game.active
            else:
                game.active = False
                if guess_button_rect.collidepoint(event.pos):  # Check if clicked on Guess button
                    game.handle_guess()
                if game.show_try_again and try_again_button_rect and try_again_button_rect.collidepoint(
                        event.pos):  # Check if clicked on Try Again button
                    game.reset_game()

            game.color = game.color_active if game.active else game.color_inactive

        if event.type == pygame.KEYDOWN:
            if game.active:
                if event.key == pygame.K_RETURN:
                    game.handle_guess()
                elif event.key == pygame.K_BACKSPACE:
                    game.text = game.text[:-1]
                else:
                    game.text += event.unicode

    game.draw()  # Draw the game
    game.update_cursor()
