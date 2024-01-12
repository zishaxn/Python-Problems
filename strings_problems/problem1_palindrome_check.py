def check_palindrome(str):
    start = 0
    end = len(str) - 1
    while start < end:
        if not (str[start] == str[end]):
            return False
        start += 1
        end -= 1
    return True


print(check_palindrome('LAL'))

# just use two pointer , and iterate simultaneously
