def reverse_whole(string):
    s = string.split()
    print(s)
    print(len(s))
    ans = ''
    for i in range(len(s) - 1, -1, -1):
        ans += s[i]
        if i != 0:
            ans += ' '  # Add a space only if it's not the last word
    return ans


# Example usage:
result = reverse_whole("Hello I am Zishan")
print(result)
