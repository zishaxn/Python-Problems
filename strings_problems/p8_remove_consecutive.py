def remove_consecutive(string):
    s = string[0]
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            s += string[i+1]
    return s

str_value = "aabbcdde"
result_str = remove_consecutive(str_value)
print(result_str)
