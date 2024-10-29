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

import tkinter as tk
import random
from tkinter import font


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.root.geometry("420x525")
        self.root.resizable(False, False)

        # Load the icon
        try:
            icon = tk.PhotoImage(file="icon.png")  # Load the icon
            root.iconphoto(False, icon)  # Set the icon
            self.icon = icon  # Keep a reference to prevent garbage collection
        except Exception as e:
            print(f"Icon not found: {e}")

        # Load the logo
        try:
            logo = tk.PhotoImage(file="numbers.png")  # Load the logo
            self.logo_label = tk.Label(root, image=logo)  # Create a label for the logo
            self.logo_label.pack(pady=10)  # Pack the label
            self.logo = logo  # Keep a reference to prevent garbage collection
        except Exception as e:
            print(f"Logo not found: {e}")

        self.target_number = random.randint(1, 100)
        self.attempts = 10
        self.remaining_attempts = self.attempts
        self.success_attempt = None

        # Custom fonts
        title_font = font.Font(size=14, weight='bold')
        normal_font = font.Font(size=12)

        # Create labels and buttons with different colors
        self.label = tk.Label(root, text="Welcome to the Number Guessing Game!\n"
                                          "Select a number between 1 and 100.\n"
                                          f"You have {self.attempts} attempts to guess the number.",
                              font=title_font, fg='blue')  # Set title font color
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=normal_font, fg='black', bg='lightgrey')  # Entry field color
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess, font=normal_font,
                                       fg='white', bg='green')  # Button colors
        self.guess_button.pack(pady=5)

        self.result_label = tk.Label(root, text="", font=normal_font, fg='red')  # Result label color
        self.result_label.pack(pady=10)

        self.attempts_label = tk.Label(root, text=f"Remaining attempts: {self.remaining_attempts}",
                                        font=normal_font, fg='orange')  # Attempts label color
        self.attempts_label.pack(pady=5)

        # Try Again button
        self.try_again_button = tk.Button(root, text="Try Again", command=self.reset_game, font=normal_font,
                                           fg='white', bg='blue')
        self.try_again_button.pack(pady=5)
        self.try_again_button.pack_forget()  # Hide the button initially

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.entry.delete(0, tk.END)

            if guess < 1 or guess > 100:
                self.result_label.config(text="Please enter a number between 1 and 100.")
                return

            self.remaining_attempts -= 1

            if guess == self.target_number:
                self.success_attempt = self.attempts - self.remaining_attempts
                self.result_label.config(
                    text=f"Congratulations! You guessed the number {self.target_number} in attempt {self.success_attempt}!",
                    fg='green')  # Change text color for correct guess
                self.guess_button.config(state=tk.DISABLED)
                self.try_again_button.pack()  # Show "Try Again" button
            elif guess < self.target_number:
                self.result_label.config(text="Your guess is too low. Try again.")
            else:
                self.result_label.config(text="Your guess is too high. Try again.")

            if self.remaining_attempts == 0:
                self.result_label.config(
                    text=f"Sorry, you've used all attempts. The correct number was {self.target_number}.",
                    fg='red')  # Change text color when out of attempts
                self.guess_button.config(state=tk.DISABLED)
                self.try_again_button.pack()  # Show "Try Again" button
            self.attempts_label.config(text=f"Remaining attempts: {self.remaining_attempts}")

        except ValueError:
            self.result_label.config(text="Please enter a valid integer.", fg='red')  # Color for invalid input

    def reset_game(self):
        self.target_number = random.randint(1, 100)
        self.remaining_attempts = self.attempts
        self.success_attempt = None

        self.entry.delete(0, tk.END)
        self.result_label.config(text="", fg='red')
        self.attempts_label.config(text=f"Remaining attempts: {self.remaining_attempts}")
        self.guess_button.config(state=tk.NORMAL)
        self.try_again_button.pack_forget()  # Hide "Try Again" button


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
