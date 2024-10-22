# https://www.codewars.com/kata/55225023e1be1ec8bc000390/train/python
# I. Jenny's secret message
# Description:
# Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
# Can you help her?


def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# https://www.codewars.com/kata/58b309e4bffc6b0a09000036/train/python
# II. Find The Distance Between Two Points
# Given two ordered pairs calculate the distance between them. Round to two decimal places.
# This should be easy to do in 0(1) timing.


import math


def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


# https://www.codewars.com/kata/587a75dbcaf9670c32000292/train/python
# III. No yelling!
# Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.
# Examples:
# filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
# filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
# filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!


def filter_words(st):
    return ' '.join(st.split()).capitalize()


# https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python
# IV. Convert a Number to a String
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?


def number_to_string(num):
    return str(num)


# https://www.codewars.com/kata/57a55c8b72292d057b000594/train/python
# V. Reversing Words in a String
# You need to write a function that reverses the words in a given string. Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
# Example (Input --> Output)
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"


def reverse(st):
    return " ".join(st.strip().split(" ")[::-1])


# https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python
# VI. Reverse List Order
# In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]


def reverse_list(l):
    return l[::-1]


# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
# VII. Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If the number is a multiple of both 3 and 5, only count it once.
# Courtesy of projecteuler.net (Problem 1)


def solution(number):
    sum = 0
    if number < 0:
        return 0
    else:
        for a in range(number):
            if a % 3 == 0 or a % 5 == 0:
                sum += a
        return sum


# https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python
# VIII. Will you make it?
# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return mpg * fuel_left >= distance_to_pump


# Respect. You have ranked up to 7 kyu in Python.

# https://www.codewars.com/kata/53af2b8861023f1d88000832/train/python
# IX. Are You Playing Banjo?
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo"
# name + " does not play banjo"


def are_you_playing_banjo(name):
    good = name + " plays banjo"
    bad = name + " does not play banjo"
    return good if name[0] == "R" or name[0] == "r" else bad


# https://www.codewars.com/kata/53369039d7ab3ac506000467/train/python
# X. Convert boolean values to strings 'Yes' or 'No’
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python
# XI. Counting sheep
# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
# For example,
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like null/undefined


def count_sheeps(sheep):
   sum = 0
   for s in sheep:
        if s:
            sum += 1
   return sum


# https://www.codewars.com/kata/is-this-my-tail/train/python
# XII. Is this my tail?
# Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.
# The arguments will always be non empty strings, and normal letters.


def correct_tail(body, tail):
    return body[-1] == tail[0]
