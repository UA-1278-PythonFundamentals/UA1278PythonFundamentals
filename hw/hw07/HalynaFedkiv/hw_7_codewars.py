def greet(name):   # Jenny's secret message
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


def distance(x1, y1, x2, y2):   # Simple: Find The Distance Between Two Points
    """ Given two ordered pairs calculate the distance between them.
    Round to two decimal places."""
    return round(pow(pow(x2-x1, 2) + pow(y2-y1, 2), 1/2), 2)


def filter_words(st):   # No yelling!
    """ Write a function taking in a string
    like "WOW this is REALLY          amazing" and returning "Wow this is really amazing".
    String should be capitalized and properly spaced. Using re and string is not allowed."""
    return ' '.join(st.split()).capitalize()


def number_to_string(num):  # Convert a Number to a String!
    """We need a function that can transform a number (integer) into a string."""
    return str(num)


def reverse(st):  # Reversing words in a String
    """You need to write a function that reverses the words in a given string.
    Words are always separated by a single space. As the input may have trailing spaces,
    you will also need to ignore unnecessary whitespace."""
    return ' '.join(st.split()[::-1])


def reverse_list(l):  # Reverse List Order
    """Create a function that takes in a list and returns a list with the reverse order."""
    return l[::-1]


def solution(number):  # Multiples of 3 or 5
    """If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
    Additionally, if the number is negative, return 0.
    Note: If the number is a multiple of both 3 and 5, only count it once."""
    return sum([num for num in range(number) if num % 3 == 0 or num % 5 == 0])


def zero_fuel(distance_to_pump, mpg, fuel_left):  # Will you make it?
    """You were camping with your friends far away from home,
    but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away!
    You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
    Considering these factors, write a function that tells you if it is possible to get to the pump or not.
    Function should return true if it is possible and false if not."""
    return mpg * fuel_left >= distance_to_pump


def are_you_playing_banjo(name):  # Are You Playing Banjo?
    """Create a function which answers the question "Are you playing banjo?".
    If your name starts with the letter "R" or lower case "r", you are playing banjo! """
    return f'{name} plays banjo' if name.startswith(('r', 'R')) else f'{name} does not play banjo'


def bool_to_word(boolean):  # Convert boolean values to strings 'Yes' or 'No'.
    """Complete the method that takes a boolean value and return a "Yes" string for true,
    or a "No" string for false."""
    return 'Yes' if boolean else 'No'


def count_sheeps(sheep):  # Counting sheep...
    """Consider an array/list of sheep where some sheep may be missing from their place.
    We need a function that counts the number of sheep present in the array (true means present)."""
    return sheep.count(True)


def correct_tail(body, tail):  # Is this my tail?
    """Some new animals have arrived at the zoo.
    The zookeeper is concerned that perhaps the animals do not have the right tails.
    To help her, you must correct the broken function to make sure that the second argument (tail),
    is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
    If the tail is right return true, else return false. The arguments will always be nonempty strings, and normal letters.
    """
    return body.endswith(tail)
