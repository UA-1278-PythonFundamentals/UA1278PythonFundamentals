import os
print(os.getcwd()+"\\hw")
for path in os.walk(os.getcwd()+"\\hw"):
    print(path)