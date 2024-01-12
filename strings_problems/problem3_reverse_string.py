def reverse_string(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' '.join(reversed_words)
    return reversed_string


# reversed_words = [word[::-1] for word in words]
#  this line takes an array or list in python then using for loop iterated over each element in list
#  and using [::-1] reverse each word in the list and then using empty string creates a new string and
#  returns it

# reversed_string = ' '.join(reversed_words)
# The join method in Python is used to concatenate elements of an iterable (such as a list) into a single string.
# It takes the form:


# Example usage
result = reverse_string("Hello i m zishan")
print("Reversed String Word By Word :" + result)


# ------------------------------------------------------------------------------------------------
def reverse_string_whole(string):
    return string[::-1]


result = reverse_string_whole("Hello i m zishan")
print("Reverse String as Whole:      " + result)
