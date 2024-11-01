# print("text")

# # print(0/0)
# print(a)
# print("end")


# print("text")
# try:
#     print(0/0)
# except Exception:
#     print("error")

# print("end")

# def input_int(text):
#     while True:
#         try:
#             result = int(input(text))
#             break
#         except Exception as err:

#             print("error", err)
#             log.error()
#     return result
# a = input_int("input a:")
# print("read:", a)



# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) 
#     if a >= 4:
#         print("Value of b = ", b) 
# except(ZeroDivisionError, NameError, ValueError):
#     print("Error Occurred and Handled")

# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) 
#     if a >= 4:
#         print("Value of b = ", b) 
# except(ZeroDivisionError, NameError, ValueError) as err:
#     if type(err) == ZeroDivisionError:
#         print("ZeroDivisionError")
#     elif type(err) ==  NameError:
#         print("NameError")
#     elif type(err) ==  ValueError:
#         print("ValueError")

# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) 
#     if a >= 4:
#         print("Value of b = ", b) 
# except ZeroDivisionError as err:
#     print("ZeroDivisionError", err)
# except (NameError, EOFError) as err:
#     print("NameError", err)
# except ValueError:
#     print("ValueError")




# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) 
#     if a >= 4:
#         print("Value of b = ", b) 

# except ZeroDivisionError as err:
#     print("ZeroDivisionError", err)
# except ArithmeticError:
#     print("ArithmeticError")
# except (NameError, EOFError) as err:
#     print("NameError", err)
# except ValueError:
#     print("ValueError")
# except:
#     print("default")
# else:
#     print("else")
# finally:
#     print("finally")

# def sum(a, b):
#     try:
#         return a+b
#     except:
#         return "Error"
#     finally:
#         # return 99
#         print(99)
    
# print(sum(5, 5))
# print(sum("5", 5))

# raise ValueError("My erre")
# raise int

from log import logging
from user import User, UserError
from random import randint

users = []
while len(users) < 10:
    try:
        users.append(User(f"name", randint(-50, 99)))
    except UserError as err:
        print(err)
print(users)
