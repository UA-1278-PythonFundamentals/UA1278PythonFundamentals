# file = open("users.txt")
# file = open("lessons\\lesson14\\users.txt")







# try:
#     file = open("lessons\\lesson14\\test.txt", "w+")
#     # print(file)
#     for i in range(20):
#         file.write(f"text_{str(i).zfill(2)}\n")
# except:
#     pass
# finally:
#     file.close()

# # print(file)

# # file.write("test")#ValueError: I/O operation on closed file

# try:
#     file = open("lessons\\lesson14\\test.txt", "r")
#     print(file.tell())
#     print(file.readline())
#     print(file.tell())
#     print(file.readline())
#     print(file.tell())
#     file.seek(20)
#     print(file.tell())
#     print(file.readline())
#     print("="*10)
#     print(file.read())
# except:
#     pass
# finally:
#     file.close()


try:
    file = open("lessons\\lesson14\\test.txt", "a")
    print(file.tell())
    file.write("tetx")
    file.seek(58)
    print(file.tell())
    file.write("FFFF")

except:
    pass
finally:
    file.close()
