# No yelling!?
def filter_words(st):
    words = st.lower().split()
    return ' '.join(words).capitalize()


print(filter_words('HELLO       CAN YOU HEAR ME')) #=> Hello can you hear me
print(filter_words('now THIS is REALLY interesting')) #=> Now this is really interesting
print(filter_words('THAT was EXTRAORDINARY!')) #=> That was extraordinary!