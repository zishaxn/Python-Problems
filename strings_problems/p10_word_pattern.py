# https://leetcode.com/problems/word-pattern/submissions/

def wordPattern(pattern, s):
    words = s.split(' ')
    if len(words) != len(pattern):
        return False
    char_to_word_map = {}
    for i in range(len(pattern)):
        curr_char = pattern[i]
        if curr_char in char_to_word_map:
            if char_to_word_map[curr_char] != words[i]:
                return False
        else:
            if words[i] in char_to_word_map.values():
                return False
            else:
                char_to_word_map[curr_char] = words[i]
    return True

pattern = 'ABBA'
string = 'DOG CAT Goat DOG'
print(wordPattern(pattern,string))
