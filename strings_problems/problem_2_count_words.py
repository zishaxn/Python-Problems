def count_word(string):
    count = 1
    for i in string:
        if i == ' ':
            count += 1

    return count


# 2nd Method is more effective as it checks actual words instead of spaces.

# first convert the string into array and the simple using len()
def count_words1(s):
    return len(s.split())


print(count_words1("Hello Everyone! How Are You"))
print(count_word("Hello Everyone! How Are You"))
