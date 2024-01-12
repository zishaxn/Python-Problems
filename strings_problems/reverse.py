def reverse_whole(string):
    arr = [0] * 256
    max_occur = ' '
    max_count = 0
    for i in string:
        print(i, end=' ')
        curr_char = i
        arr[ord(curr_char)] += 1

        if arr[ord(curr_char)] > max_count:
            max_count = arr[ord(curr_char)]
            max_occur = curr_char
    return max_occur


str = "ABAACSSAAAAB"
str = reverse_whole(str)
print(str)
