

# a = int(input("a:"))
# s = 0
# while a>0:
#     s += a
#     a = int(input("a:"))

# print(f"{s=}")


# l = [1,2,3,4,5]
# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])


# start = 0
# finish = 10
# iter = 0
# while start < finish:
#     print(iter, start)
#     # start += 1
#     iter += 1
# else:
# #     print ("The end")
# import time

# from datetime import date, datetime, timedelta

# while True:
#     pass

# l = [10, None, [1, 5, 6], "test",(2, "a", 5.6), {1,2,3,1,2,3}]


# for element in l:
#     if type(element) in (list, tuple):
#         for e in element:
#             print("\t", e)
#     else:
#         print(element)
    
# s = set("vgdhsbfsdjnbfkjsdbvfsdbfjkdikj")
# print(s)
# for c in s:
#     print(c)

# d = {
#     "key1": "value1",
#     15: "value2",
#     "key2": "value3"
# }
# print(d)
# for i in d:
#     print(i, d[i])

# a, b = (1, 5)
# print(d.items())
# print(a, b)
# for key, value in d.items():
#     print(key, value)

# l = [1,2,4,423,4,325,43,51,24,543,65,3245,76]
# # for element in l:
# #     print(element)

# for i in range(len(l)):
#     print(f"l[{i}]={l[i]}")

# n = 5
# l = [i for i in range(n)]
# t = (i for i in range(n))
# print(f"{n=}")
# print(l.__sizeof__())
# print(t.__sizeof__())
# n = 500
# l = [i for i in range(n)]
# t = (i for i in range(n))
# print(f"{n=}")
# print(l.__sizeof__())
# print(t.__sizeof__())
# n = 50000
# l = [i for i in range(n)]
# t = (i for i in range(n))
# print(f"{n=}")
# print(l.__sizeof__())
# print(t.__sizeof__())
# r = range(3)
# print(list(r))
# r = range(-3)
# print(list(r))
# r = range(-5, 3)
# print(list(r))
# r = range(-5, 3, 3)
# print(list(r))

# r = range(2, -5, -1)
# print(list(r))


# l = [1,2,4,423,4,325,43,51,24,543,65,3245,76]

# print(l[5])
# print(len(l))
# l = [1,2,4,423,4,325,43,51,24,543,65,3245,76]
# for i in range(len(l)):
#     print(l[i])
# print(enumerate(l))
# print(list(enumerate(l)))
# for i, element in enumerate(l):
#     print(i, element)

# print(list(range(0,15))[::-1])

# print("i\ti**2\ti**i")
# for i in range(5):
#     print(i, end="\t")
#     print(i**2, end="\t")
#     print(i**i)


# for i in range(10):
#     print(i, end="")
#     if i%2==0:
#         print()
#         continue
#     print("=>", i**i)

# for i in range(10):
#     print(i, end="")
#     if i==3:
#         print()
#         break
#     print("=>", i**i)


# for i in range(5):
#     print(i)
#     for j in range(5):
#         print("\t",j)
#         if i+j >4:
#             break

# l = [1,5,9]#"a8",6,9, [1,"8", 9], "text"]
# s = 0
# temp = None
# for i in l:
#     if type(i) is not int:
#         temp = i
#         continue
#     s += i

# print("end")

# print(temp)

# print(__name__)
# if __name__ == "__main__":
#     print("test")


# for i in range(0, 100, 2):
#     print(i)

# i = 0
# while i < 100:
#     if i % 2 == 0:
#         print(i)
#     i += 1
# for i in range(1, 100, 2):
#     print(i)

# i = 1
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)


l = [2, 4,5, 6]
i = 0
while i < len(l):
    if l[i] % 2 == 1:  # Перевіряємо елемент списку на непарність
        print("Has odd numbers")
        break

    print("Does not have odd numbers")
    i += 1
