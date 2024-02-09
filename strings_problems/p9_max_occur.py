def max_ocurr(string):
    arr = [0]*256  # creating a 256 size array
    max_count = -1
    max_ocurr = ' '

    for i in string:
        curr_char = i

        arr[ord(curr_char)]+=1

        if arr[ord(curr_char)]>max_count:
            max_count = arr[ord(curr_char)]
            max_ocurr = curr_char

    return max_ocurr

s = "acccbbaba"

print(max_ocurr(s))
