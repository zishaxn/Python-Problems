word = "UsA"
def is_capital(word):
    if word.isupper() or word.islower():
        return True
    else:
        temp_word = word.capitalize()
        if word[0] != temp_word[0]:
            return False
        for char in range(1, len(word)):
            if word[char].isupper():
                return False
    return True
