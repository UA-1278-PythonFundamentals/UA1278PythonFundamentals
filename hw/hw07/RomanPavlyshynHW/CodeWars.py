########Task1##########
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)

#########Task2#############
def distance(x1, y1, x2, y2):
    return round(((x2-x1)**2 + (y2-y1)**2)**0.5, 2)

#########Task3#############
# def filter_words(st):
#     word = st.lower().split()
#     first = word[0].capitalize()
#     sl = " ".join(word[1:])
#     return first +" " + sl
#########Task4#############
# def number_to_string(num):
#     return str(num)

#########Task5#############
# def reverse(st):
#     words = st.strip().split()
#     # Reverse the list of words
#     reversed_words = " ".join(reversed(words))
#     return reversed_words

#######Task6##########
# def reverse_list(l):
#     return l[::-1]
# #######Task7##########
# def solution(number):
#     counter = 0
#     if number <= 0:
#         return 0
#     for i in range(number):
#         if i %3 == 0 or i %5 == 0:
#             counter+=i
#     return counter
#
# ######Task8##########
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if fuel_left*mpg >= distance_to_pump:
#         return True
#     else:
#         return False

#########Task9###########
# def are_you_playing_banjo(name):
#     if name[0] == "R" or name[0] == 'r':
#         return f"{name} plays banjo"
#     else:
#         return f"{name} does not play banjo"

#########Task10###########
# def bool_to_word(boolean):
#     if boolean == True:
#         return 'Yes'
#     else:
#         return "No"

#############Task11###############
# def count_sheeps(sheep):
#     count = 0
#     for i in sheep:
#         if i == True:
#             count += 1
#
#     return count

#############Task12###############
# def correct_tail(body, tail):
#     t = len(tail)
#     sub = body[-t]
#     return sub == tail