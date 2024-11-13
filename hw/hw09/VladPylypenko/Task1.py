import random

number_rand = random.randint(0,10)
tries = 6

while True:
    a = (int(input("\n Write your number: ")))

    if a < number_rand:
        tries -=1
        print("Not bad, but your number is less, then mne")
        print("your tries: ", tries)
    if a > number_rand:
        tries -=1
        print("Not bad, but your number is more, then mne")
        print("your tries: ", tries)
    if a == number_rand:
        print("Congratulations, you did it)")
        print("tries you have left: ", tries)
        break
    if tries == 0:
        print("you havent any chance(")
        break


