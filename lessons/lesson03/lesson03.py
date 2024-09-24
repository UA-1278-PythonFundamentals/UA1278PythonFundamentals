# t = True
# print(type(t), t)
# t = False
# print(type(t), t)
# # t = 156**555
# t = 156
# print(type(t), t)
# t = 55.5
# print(type(t), t)
# t = [55.5, 5]
# print(type(t), t)
# t = (55.5, 5)
# print(type(t), t)
# t = "cgsdicnfkdsfbod"
# print(type(t), t)
# t = 'c'
# print(type(t), t)

# t = '''c'''
# print(type(t), t)

# t = {1,2,3,4,1,2,3,1,2}
# print(type(t), t)

# t = set("bbfckjdsbfhsdvbjchsdhfvasdjhfvsdvfjhsdvfdvsjfsdj")
# print(type(t), t)
# int
# t = {
#     "key": "value1",
#     1: "value2",
#     "key2": "value1",
#     "key": "copy value",
# }
# print(type(t), t)

# a = "55"
# print(id(a), a)
# a = a + "5"
# print(id(a), a)
# a = (1,2,3)
# print(id(a), a)
# a[1] = 10

# a = [1,2,3]
# print(id(a), a)
# a.append(55)
# print(id(a), a)
# a[1] = 10
# print(id(a), a)

# a = "55"
# b = a
# print(id(a), a)
# print(id(b), b)
# a = a + "5"
# print(id(a), a)
# print(id(b), b)

# for i in range(2):
#     print(i, id(i))
# for i in range(2):
#     print(i, id(i))

# for i in range(2000,2002):
#     print(i, id(i))
# for i in range(2000,2002):
#     print(i, id(i))

# a1 = "988989"
# a2 = "988989"
# a3 = 988989
# print(id(a1))
# print(id(a2))
# print(id(a3))
# a1 = 55
# print(id(a1))
# print(id(a2))
# print(id(a3), type(a3))

# print(type(a3) is int)
# print(type(a3) is float)
# a3 = 3.3
# print(type(a3) is float)
# print(isinstance(a3, float))

# class A: pass
# class B(A): pass
# a = A()
# b = B()
# c = 1
# print(type(a) is A)
# print(type(b) is A)

# print(isinstance(a,A))
# print(isinstance(b, A))
# print(isinstance(c, A))

# a = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
# print(a)

# a = 1 + 2 + 3\
#       + 4 + 5 +\
#           6 + 7 + 8 + 9
# print(a)

# a = (1 + 2 + 3
#       + 4 + 5 +
#     6 + 7 + 8 + 9)
# print(a, type(a))
# a = [1 + 2 + 3
#       + 4 + 5 +
#     6 + 7 + 8 + 9]
# print(a, type(a))

# l = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# a = 1
# print(a)
# b = a+2
# print(a, b)
# a = 1;print(a); b = a+2; print(a, b)

# for i in range(5):
#  print(i, end=" => ")
#  print(i+1, end=" => ")
#  print(i+2)
# for i in range(5):
#       print(i, end=" => ")
#       print(i+1, end=" => ")
#       print(i+2)

# a = 1
# b = 2
# c = 3
# print(a,b,c)
# a,b,c = 10, 55, 99
# print(a,b,c)
# l = [1,2,3]
# q,w,e = l

# print(q,w,e)
# q = l[0]
# w = l[1]
# e = l[2]

# a = 1
# b = 2

# print(a, b)
# # c = a
# # a = b
# # b = a
# a, b = b, a
# print(a, b)

# a = 0b1010101010
# print(a)
# a = 0o01234567
# print(a)
# a = 0x0123456789abcdef
# print(a)
# a = 555
# print(bin(a))
# print(oct(a))
# print(hex(a))

# a = 1_0_0_0_000_000_000
# print(type(a), a)

# a = 120.5
# print(type(a), a)
# a = .5
# print(type(a), a)
# a = 120.
# print(type(a), a)

# a = 15e2
# print(a)
# a = 15e-2
# print(a)


# print((-1)**0.5)

# print(True == 1)
# print(False == 0)

# l = [1, "test", 5.6, (1,2), None]
# print(l)
# for i in l:
#     print(i, type(i))
# d = {}
# d[[152]] = 5

# t = (1,2,3,4)
# print(t.__hash__())
# print(t.__hash__())
# print(t.__hash__())
# print(t.__hash__())
# print(t.__hash__())
# print(t.__hash__())


# for i in range(100):
# #     print(f"{i} {chr(i)}")
# s = "jhfsdfhdsgfsdg1651651"
# for i in s:
#     print(f"{i} {ord(i)}")


# a = int("15")
# print(type(a), a)
# a = int(15.1)
# print(type(a), a)
# a = int(15.9)
# print(type(a), a)


# a = int("15", 8)
# print(type(a), a)
# a = int("15", 16)
# print(type(a), a)
# a = int("111", 2)
# print(type(a), a)
# a = int("09az", 36)
# print(type(a), a)

# text = "test\ntest"
# print(text)
# text = "test\rab"
# print(text)
# text = "test\ttest"
# print(text)
# text = "test\"test"
# print(text)
# text = "test\\test"
# print(text)

# template = "my name is %s. my age is %d"

# print(template)
# print(template % ("Liubomyr", 38))
# print(template % ("Anna", 15))
# print(template % ("Anry", 95))
# print(template % ("Vira", 15))

# template = "my name is {}. my age is {}"
# print(template.format("Liubomyr", 38))
# template = "{0}my name is {1}. my age is {0}"
# print(template.format("Liubomyr", 38))
# template = "my name is {name}. my age is {age}"
# print(template.format(name="Liubomyr", age=38))
# print(template.format( age=38, name="Liubomyr"))

# name = "liUboMyr"
# age=38
# print(f"my name is {name.title()}. my age is {age/2}")


# s = "We can access individual characters using indexing"

# print(s[0])
# print(s[1])
# print(s[-1])
# print(s[0: 10])
# print(s[: 10])
# print(s[5:])
# print(s[:])
# print(s[::2])
# print(s[::-1])

# s = "1sssssssssssssssssssfdsfdsfssssssssssssssfdgfdgssssssssssssssssssssssssssssss1"
# print(">", s.center(55), "<")
# print(s.count("s"))
# print(s.count("sf"))
# print(s.find("sf"))
# print(s.find("sf", s.find("sf")+1))
# print(s.index("sf"))
# s = "         uihbjnk     "
# print(s)
# print(s.strip())

# print("=>".join("dshvcjhsd"))
# s = "d=>s=>h=>v=> c=>j=>h= >s=>d"
# print(s.split())
# print(s.split("=>"))
# print(s.replace("=>", "--->"))

print(dir(str))
a = 1
print(dir())

