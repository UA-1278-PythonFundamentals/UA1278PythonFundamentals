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

import random


class Colors:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BROWN = "\033[33m"
    RESET = "\033[0m"  # Reset to default color


def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 10

    print(f"\n{Colors.BLUE}Welcome to the Number Guessing Game!{Colors.RESET}")
    print(f"{Colors.BROWN}Select a number between 1 and 100.{Colors.RESET}")
    print(f"{Colors.GREEN}You have {attempts} attempts to guess the number.{Colors.RESET}\n")

    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"{Colors.YELLOW}Attempt {attempt}: Enter your guess: {Colors.RESET}"))
                if guess < 1 or guess > 100:
                    print(f"{Colors.RED}Please enter a number between 1 and 100.{Colors.RESET}")
                    continue
                break

            except ValueError:
                print(f"{Colors.RED}Please enter a valid integer.{Colors.RESET}")

        if guess == target_number:
            print(
                f"{Colors.GREEN}Congratulations! You guessed the number {target_number} correctly in {attempt} attempts.{Colors.RESET}")
            break
        elif guess < target_number:
            print(f"{Colors.RED}Your guess is too low. Try again.{Colors.RESET}")
        else:
            print(f"{Colors.RED}Your guess is too high. Try again.{Colors.RESET}")
    else:
        print(
            f"{Colors.RED}Sorry, you've used all {attempts} attempts. The correct number was {target_number}.{Colors.RESET}")


number_guessing_game()
