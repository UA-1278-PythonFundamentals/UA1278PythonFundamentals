import random

print("Guess a number from 1 to 100. You have 10 attempts")
run_num = random.randint(1,100)


for i in range(10):
    n = int(input())
    if n > run_num:
        print("Your number is greater than guessed number")
        continue
    elif n < run_num:
        print("Your number is less than guessed number")
        continue
    elif n < 1 or n > 100:
        print("You out of range. You must be in range from 1 to 100")
        continue
    elif n == run_num:
        print("congratulations! You win the game")
        break
else:
    print("You lost the game!")

