# Permutations of each other
# Two strings are said to be a permutation of each other when either of the string's
# characters can be rearranged so that it becomes identical to the other one.
#
# Example:
# str1= "sinrtg"
# str2 = "string"
#
# The character of the first string(str1) can be rearranged to form str2 and hence we can say that the given strings
# are a permutation of each other.

def is_permutation(stringIn, string2):
    s1 = set(string1)
    s2 = set(string2)
    if len(s1) > len(s2) or len(s2) > len(s1):
        return False
    for i in s1:
        if not s2.__contains__(i):
            return False
    return True


string1 = "ABCE"
string2 = "CABED"

print(is_permutation(string1, string2))
# is_permutation(string1,string2)
