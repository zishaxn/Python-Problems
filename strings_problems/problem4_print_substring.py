def print_substring_brute_force(string):
    n = len(string)
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(string[i:j])


print_substring_brute_force('ABC')


def print_substring_optimized(string):
    n = len(string)
    for i in range(n):
        substring = ''
        for j in range(i, n):
            substring += string[j]
            print(substring)

print('----------------------------------------')
print_substring_optimized('ABC')
