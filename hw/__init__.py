import os

# print(os.getcwd() + "\\hw")
d = {}
for path in os.walk(os.getcwd() + "\\hw"):
    s_path = path[0].split("\\")
    if len(s_path) == 7:
        # print(s_path)
        if s_path[6] in d:
            d[s_path[6]].append(s_path[5])
        else:
            d[s_path[6]] = [s_path[5]]
from pprint import pprint
pprint(d)