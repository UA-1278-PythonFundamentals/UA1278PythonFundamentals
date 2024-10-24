from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint


TRIES = 10


def start_game():
    global number, attempts

    attempts = 0
    number = randint(1, 100)
    entry.delete(0, END)
    label.config(text="Enter a number between 1 and 100")


def check_guess():
    global attempts

    guess = entry.get()

    if not guess.isdigit():
        messagebox.showerror("Error", "Please enter a number")
        return
    elif not 1 <= int(guess) <= 100:
        messagebox.showerror("Error", "Please enter a number between 1 and 100")
        return

    guess = int(guess)

    attempts += 1

    if attempts < TRIES:
        if guess == number:
            messagebox.showinfo("Congratulations", "You guessed the number")
            start_game()
        elif guess < number:
            label.config(
                text=f"Number is bigger than {guess}. Attempts left: {TRIES - attempts}"
            )
            entry.delete(0, END)
        else:
            label.config(
                text=f"Number is smaller than {guess}. Attempts left: {TRIES - attempts}"
            )
            entry.delete(0, END)
    elif attempts == TRIES:
        messagebox.showinfo("Game Over", f"The number was {number}")
        start_game()


root = Tk()
root.geometry("500x300")
root.title("Guess the number")


label = Label(root, text="Enter a number between 1 and 100")
label.pack()


entry = Entry(root)
entry.pack()

check_btn = Button(root, text="Check", command=check_guess)
check_btn.pack()


start_game()

root.mainloop()
