# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"

    return f"Hello, {name}!"

print(greet(name='Johnny'))

# II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    d = ((x2 - x1) ** 2 + (y2 - y1) **2) ** 0.5
    return round(d, 2)

print(distance(2,3,-4,2))

# III. No yelling!
def normal_string(string='WOW this is REALLY          amazing'):
    s = string.capitalize()
    new_s = ''
    for i in s.split():
       if not i.isspace():
           new_s += i + ' '
    return new_s.rstrip()

print(normal_string())

# IV. Convert a Number to a String
def number_to_string(num):
    return str(num)

print(number_to_string(123))

# V. Reversing Words in a String
def reverse(s = 'Hi There.'):
    s2 = s.split()
    s2[-1], s2[0] = s2[0], s2[-1]
    l = ' '.join(s2)
    return l

print(reverse())

# VI. Reverse List Order
def reverse_list(l):
    'return a list with the reverse order of l'
    return l[::-1]

print(reverse_list([1,23,45,5]))

# VII. Multiples of 3 or 5
def solution(number = 10):
    summa = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            summa += i
        if number < 0:
            return 0
    return summa

print(solution())

# VIII. Will you make it?
def zero_fuel(distance_to_pump = 100, mpg = 50, fuel_left = 2):
    return True if distance_to_pump <= mpg * fuel_left else False

print(zero_fuel())

# IX. Are You Playing Banjo?
def are_you_playing_banjo(name = 'bravo'):
    name_list = list(name)
    if name_list[0] == 'R' or name_list[0] == 'r':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'

print(are_you_playing_banjo())

# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean = False):
    return 'Yes' if boolean else 'No'

print(bool_to_word())

# XI. Counting sheep
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
        else:
            continue
    return count

print(count_sheeps(
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
))


# XII. Is this my tail?
def correct_tail(body, tail):
    return True if body[-1] == tail else False

print(correct_tail("Fox", 'x'))

