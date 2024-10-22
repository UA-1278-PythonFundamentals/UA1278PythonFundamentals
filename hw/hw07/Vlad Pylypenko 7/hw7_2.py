# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


# Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


# No yelling!
def filter_words(st):
    st = " ".join(st.split())
    st = st.lower()
    st = st.capitalize()
    return st


# Convert a Number to a String
def number_to_string(num):
    return str(num)


# Reversing Words in a String
def reverse(st):
    st = st.split()
    st.reverse()

    return " ".join(st)


# Reverse List Order
def reverse_list(l):
    return l[::-1]


# Multiples of 3 or 5
def solution(number):
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])


# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump <= (mpg * fuel_left) else False


# Are You Playing Banjo?
def are_you_playing_banjo(name):
    return name + " plays banjo" if name.startswith(("R", "r")) else name + " does not play banjo"


# Convert boolean values to strings Yes or No
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# Counting sheep
def count_sheeps(sheep):
    return sheep.count(True)


# Is this my tail?
def correct_tail(body, tail):
    return body[-1] == tail