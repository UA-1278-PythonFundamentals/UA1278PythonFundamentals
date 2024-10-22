import re


text = """
The programming language Python was conceived in the late 1980s,[1] and its implementation was started in December 1989[2] by Guido van Rossum at CWI in the Netherlands as a successor to ABC capable of exception handling and interfacing with the Amoeba operating system.[3] Van Rossum is Python's principal author, and his continuing central role in deciding the direction of Python is reflected in the title given to him by the Python community, Benevolent Dictator for Life (BDFL).[4][5] (However, Van Rossum stepped down as leader on July 12, 2018.[6]). Python was named after the BBC TV show Monty Python's Flying Circus.[7]

Python 2.0 was released on October 16, 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode, along with a change to the development process itself, with a shift to a more transparent and community-backed process.[8]

Python 3.0, a major, backwards-incompatible release, was released on December 3, 2008[9] after a long period of testing. Many of its major features have also been backported to the backwards-compatible, though now-unsupported, Python 2.6 and 2.7.[10]"""


pattern = "\d{2,4}"

result = re.findall(pattern, text)

print(result)

def validate_full_name(full_name):
    p = "^[A-Z][a-z]+(?: [A-Z][a-z]+)*$"
    if re.match(p, full_name):
        return True
    else:
        return False
    
print(validate_full_name("Liubomyr halamaha"))
print(validate_full_name("Liubomyr Halamaha"))
print(validate_full_name("Liubomyr1 Halamaha"))
print(validate_full_name("Liubomyr Fo"))


from own.weather import API_KEY

import own.weather

own.weather.API_KEY


import own.weather as ow

own.API_KEY

from own import weather

weather.API_KEY