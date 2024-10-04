

# ## list

# l =  list()
# print(type(l), l)
# # l =  list(1) #TypeError: 'int' object is not iterable
# l =  list("123456778")
# print(type(l), l)


# l =  []
# print(type(l), l)
# l =  [0,1,2,"test", [1,2,3]]
# print(type(l), l)

# for i in l:
#     print(type(i), i)

# print(l[1])
# l[1] = "test2222"
# print(l)
# l[-1][0] = "222"
# print(l)

# text = input("numbers:")
# print(type(text), text)
# l = text.split(",")
# for i in l:
#     i.strip()
#     print(type(i), i, end=" => ")
#     if i.isdigit():
#         i = int(i)
    
#     print(type(i), i)
# l =  [0,1,2,3,4,5,6, "test", [1,2,3]]

# print(l[2:-2])
# print(l[2::3])

# print(l[:-3] + l[5:1:-1])
# print(l*5)

# l1 = [1,2,3]
# l2 = [3,2,1]

# print(l1 ==l2)
# print(l1 ==l2[::-1])
# print([method for method in dir(list) if not method.startswith("_")])

# l = [0,1,2,3,4,5,6, "test", [1,2,3]]

# l.append(1)
# l.append([1,2,3,4,5])
# l.append("abc")
# print(l)
# # l.extend(1)#TypeError: 'int' object is not iterable
# l.extend([1,2,3])
# l.extend("abc")
# print(l)


# l.insert(1,1)
# print(l)
# l.insert(4,[1,2,3,4,5])
# print(l)
# l.insert(-2,"abc")
# print(l)

# l.insert(555,"abc")
# print(l)

# print(l.count(1))
# element = l.remove(1)
# print(element,l)
# element = l.pop()
# print(element, l)
# element = l.pop(5)
# print(element, l)

# i = l.index(1)
# print(i)
# i = l.index(1, i+1)
# print(i)
# # i = l.index(1, 2, 8) #ValueError: 1 is not in list
# i = l.index(1, 10, 13) #ValueError: 1 is not in list
# print(i)
# l.reverse()
# print(l)
# rl = list(reversed(l))
# rl = list(l[::-1])
# print(l)
# print(rl)
# l.sort(key=lambda e: id(e))
# def f(e):
#     return id(e)
# l.sort(key=f)
# print(l)
# l = [1,2,4,2,6,8,3,5]
# print(l)
# l.sort()
# print(l)
# l = list("bsaildkjnv bjhsdnvbjhdfnkbgj")
# print(l)
# l.sort()
# print(l)
# print(sorted(l, reverse=True))
# print(l)


# l = [0,1,2,3,4,5,6, "test", [1,2,3]]
# print(id(l), l)
# l.clear()
# print(id(l), l)
# l = [0,1,2,3,4,5,6, "test", [1,2,3]]
# print(id(l), l)
# l = []
# print(id(l), l)

# l = [1,2,3]
# k = [10,20,30]
# g = [1,2,3, l, k]
# print(l,  k, g)
# l.append(1)
# print(l,  k, g)
# l = []
# k.clear()
# print(l,  k, g)


# l = [1,2,3]
# k = [10,20,30]
# g = [1,2,3, l, k]

# gg = g.copy()
# print(g)
# print(gg)
# g[1] = 100
# gg[2] = 300
# g[3][1] = "a"
# k[1] = "test" 
# print(g)
# print(gg)

# import copy
# ggg = copy.deepcopy(g)

# g[1] = 100
# gg[2] = 300
# ggg[3][1] = "b"

# print(g)
# print(gg)
# print(ggg)

# print(all([1,2,3]))
# print(all([1,2,3, []]))
# print(any([1,2,3, []]))
# print(any([0,"", []]))
# print(list(enumerate([0,"", []])))
# print(len([0,"", []]))


# l = [i**3 for i in range(5)]
# l = [(i, j, i**j) for i in range(5) for j in range(5)]
# print(l)
# l = []
# for i in range(5):
#     for j in range(5):
#         l.append((i, j, i**j) )
# print(l)

# # print(sum(["1", "2"]))

# print(sum(map(int, ["1", "2"])))
# print(min(["1", "2", 1]))


## tuple


# t =  tuple()
# print(type(t), t)
# t =  tuple("shfbkds")
# print(type(t), t)
# t = ()
# print(type(t), t)
# t = (1)
# print(type(t), t)
# t = (1,)
# print(type(t), t)
# t = (1,"afdas")
# print(type(t), t)

# t = (1,2,3,4,[1,2,3])
# print(type(t), t)
# print(t[1])
# print(t[1:3])
# # t[1] = 1 #TypeError: 'tuple' object does not support item assignment
# print(t[4])
# t[4][1] = 22
# print(t)
# # t[4] = [] #TypeError: 'tuple' object does not support item assignment
# l = list(t)
# print(l)
# print([method for method in dir(tuple) if not method.startswith("_")])


## set

# s = set()
# print(type(s), s)

# text = 
# s = set("zdghjcjkvbxnkldsbfvkjsdnbvhjdaknbvjdnbvsdksnbcvfndsc hjndcbvjhcnbxhvjndzjv msfnd")
# print(type(s), s)

# # s = {} #<class 'dict'> {}
# print(type(s), s)


# s = {1,2,1,2,3,2,1,2,3,2}
# print(type(s), s)
# print([method for method in dir(set) if not method.startswith("_")])

# s.add("a")
# s.add("aaa")
# print(s)

# e = s.pop()
# print(e, s)
# e = s.remove("a")
# print(e, s)

# s.update(["1","2","3"])
# print(s)

# print("1" in s)

# l = [1,2,3,4,6,3,2,4,3,1,5]

# s = set(l)
# print(s)
# not_unic = {}
# for i in s:
#     c = l.count(i)
#     if c > 1:
#         not_unic[i] = c
# print(not_unic)


## dict

# d = dict()
# print(type(d), d)
# # d = dict([1,2,3])#TypeError: cannot convert dictionary update sequence element #0 to a sequence
# d = dict([("k1", "va1"), [1, 2], "ab"])#TypeError: cannot convert dictionary update sequence element #0 to a sequence
# print(type(d), d)

# d = {}
# print(type(d), d)

# d = {
#     "key":"value",
#     10: "text",
#     "l": 255
#     }
# print(type(d), d)

# print(d["key"])
# print(d[10])
# d["key"] = 55
# print(d)
# d["key99"] = 78
# print(d)
# # d["key9955"] #KeyError: 'key9955'


# print([method for method in dir(dict) if not method.startswith("_")])


# d = {
#   "Germany": "Berlin", 
#   "Italy": "Naples", 
#   "England": "London"
# }

# print(d.get("Germany"))
# print(d.get("Ger"))
# print(d.get("Ger", 555))
# print(d.get("Germany", 555))

# print(d.keys())
# print(d.values())
# print(d.items())
# print(d.popitem(), d)
# country_capitals = {
#   "United States": "Washington D.C.", 
#   "Italy": "Rome" 
# }

# d.update(country_capitals)
# print(d)

# for i in d:
#     print(i, d[i])

# a, b = 1, 2
# for key, value in d.items():

#     print(key, value)
#     print(key, d[key])

# print(d)
# d["United States"] = 555
# print(d)

l = ["1", "5", "9"]

m = list(map(int, ["1", "5", "9"]))
print(l)
print(m)

mm = []
for i in l:
    m.append(int(i))



l = list(set("sdfgdsgfd"))
print(l)
t = list(enumerate(l))
print(t)
l.append(10)
print(l)
print(t)
print(list(enumerate(l)))
l.append(t)
print(l)