# Reversing Words in a String
def reverse(st):
    words = list(st.split())
    
    return ' '.join(words[::-1])

print(reverse("Hello World")) # --> "World Hello"
print(reverse("Hi There.")) #  --> "There. Hi"
print(reverse(" Hi   There.  ")) #  --> "There. Hi"