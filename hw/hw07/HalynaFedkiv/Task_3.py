def count_characters(text):
    '''Calculates the number of characters
    included in a given string. Returns a dictionary with a character as a key.'''
    return {character: text.count(character) for character in text}


print(count_characters('tabb7654477cyyccddd  d'))

