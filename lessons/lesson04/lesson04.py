# a = 1
# b = 2
# print(a==b)
# print(a>b)
# print(a<b)

# a = [1,2,3]
# b = [2,3,1]
# c = [1,2,3,"3"]
# print(f"{a==b=}")
# print(f"{a==c=}")
# print(f"{a>b=}")
# print(f"{a<b=}")
# print(f"{[1,2,3] == 1=}")
# print(f"{[1,2,3] == 1=}")

# print(True and True or True and False)
# print(True and (True or True and False))
# print(10 and (20 or "True" and []))
# print(10 and "a" and "g")
# print(10 and [] and 0 and "g")
# print([] or "" or 0)
# print([] or "x" or 55 or 0)
# is_false = [False, None, 0, "", [], (), {}]
# if len([]) > 0: pass
# if []: pass

# a = [1,2,3]
# b = [1,2,3]
# c = a
# print(f"{a==b =}")
# print(f"{a==c =}")
# print(f"{a is b =}")
# print(f"{a is c =}")
# print(f"{id(a) == id(c) =}")
# print(f"{id(a) == id(b) =}")

# a = 1000
# b = 1000
# print(a is b)
# b = 0
# for i in range(300):
    
#     print(i, i is b)
#     b += 1




# a = [1,2,"3", [99, 88]]

# print(f"{1 in a =}")
# print(f"{10 not in a =}")
# # print(f"{10 not in 10 =}")
# print(f"{99 in a =}")
# print(f"{[99, 88] in a =}")
# print(f"{[99] in a =}")


# a = 15
# if a > 20:
#     print("if is true")
#     print("a is", a)

# print("end")

# age = int(input("my age: "))
# if age >= 18 and age < 65: 
#     print("is worker")

# if  17 < age < 65: 
#     print("is worker")
# a =1
# b=2
# c=3
# d=4
# if a < b < c < d:
#     print("true")

# age = int(input("my age: "))
# if age >= 18 and age < 65: 
#     print("is worker")
# else:
#     print("is not worker")



# age = int(input("my age: "))
# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')

# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')

# weather = "raining"
# result = "Open Your umbrella" if weather == "raining" else "Wear your cap"
# print(result)
# weather = "not raining"
# result = "Open Your umbrella" if weather == "raining" else "Wear your cap"
# print(result)
# # result =  weather == "raining" ? "Open Your umbrella" : "Wear your cap"
# result = None
# if weather == "raining":
#     result = "Open Your umbrella"
# else:
#     result = "Wear your cap"

# from datetime import date, datetime, timedelta

# d = date.today()
# print(d)
# dt = datetime.now()
# dt1 = datetime.now()
# dt2 = datetime.now()

# dt1 += timedelta(days=10)
# dt2 -= timedelta(days=10)

# print(dt)
# print(dt1)
# print(dt2)
# print(dt > dt1)
# print(dt > dt2)
# print(dt.timestamp())

# status = int(input("http status code: "))
# match status:
#     case 400:
#         print("Bad request")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")

# if status == 400:
#     print("Bad request")
# elif status ==  401:
#     print("Unauthorized")
# elif status == 403:
#     print("Forbidden")
# elif status == 404:
#     print("Not found")
# else:
#     print("Other error")

# match status:
#     case 400:
#         print("Bad request")
#     case 401 | 403 as error:
#         print(f'{error} is authentication error')
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")

# if status == 400:
#     print("Bad request")
# elif status ==  401 or status == 403:
#     print(f'{status} is authentication error')
# elif status == 404:
#     print("Not found")
# else:
#     print("Other error")


# values = input("enter values: ").split()
# match values:
#     case "load", link:
#         print(" load -> ", link)
#     case "save", link, filename:
#         print(f"save({link}, {filename})")
#     case "save", link, *filenames:
#         print(f"save:")
#         for filename in filenames:
#             print(f"\t({link}, {filename})")
#     case _:
#         print(f"default({values})")

# if len(values) == 2 and values[0] == "load":
#     print(" load -> ", values[1])
# elif len(values) == 3 and values[0] == "save":
#     print(f"save({values[1]}, {values[2]})")
# elif len(values) > 3 and values[0] == "save":
#     print(f"save:")
#     for filename in values[2]:
#         print(f"\t({values[1]}, {filename})")
# else:
#     print(f"default({values})")

# a = 15
# b = 10
# if a == b:
#     print("a = b")
# elif a > b:
#     print("a > b")
# else:
#     print("a < b")

# int1 = int(input("Enter the first number: "))
# int2 = int(input("Enter the second number: "))

# if int1 == int2:
#     print("Equal")
# elif int1 > int2:
#     print(f"{int1} is bigger than {int2}")
# else:
#     print(f"{int2} is bigger than {int1}")
# Введення двох чисел
# num1 = float(input("Введіть перше число: "))
# num2 = float(input("Введіть друге число: "))
# # Порівняння чисел
# if num1 > num2:
#     print(f"{num1} більше ніж {num2}")
# elif num1 < num2:
#     print(f"{num1} менше ніж {num2}")
# else:
#     print(f"{num1} дорівнює {num2}")


# # Введення числа
# number = int(input("Введіть число: "))
# # Перевірка парності
# if number % 2 == 0:
#     print(f"{number} є парним числом")
# else:
#     print(f"{number} є непарним числом")


# a = 10
# if a % 2 == 0:
#     print("парне")
# else:
#     print("не парне")

a = (1,2,[3])
# a = (1,2,[3])
# b = [1,2,3]
# c = a
# print(id(a))
# print(id(b))
# print(id(c))

# a != b

print(id(a))

class A:pass
a = A()
print(a)
print(id(a))