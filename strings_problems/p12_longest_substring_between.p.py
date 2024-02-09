# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

def maxLengthBetweenEqualCharacters(s):
    for i in range(len(s)):
        end = len(s) - 1
        while i < end:
            c1 = s[i]
            c2 = s[end]
            if c1 == c2:
                return end - i - 1
            else:
                end -= 1
    return -1


s = "ABCDB"


def maxLengthBetweenEqualCharacters1(s):
    map_chars = {}
    max_length = -1
    for i in range(len(s)):
        curr_char = s[i]
        if s[i] in map_chars:
            last_index_present = map_chars[curr_char]
            max_length = max(max_length, i-last_index_present - 1)
        else:
            map_chars[curr_char]=i
    return max_length


print(maxLengthBetweenEqualCharacters1(s))
