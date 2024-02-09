def checkPalindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        # Skip symbols and whitespaces
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1
        # Convert characters to lowercase for case-insensitivity
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True

s= 6
s1 = 'c1 O$d@eeD o1c'
s2= 'N2 i&nJA?a& jnI2n'
s3= 'A1b22Ba'
s4= 'codingninjassajNiNgNidoc'
s5 = '5?36@6?35'
s6 = 'aaBBa@'

print(checkPalindrome(s2))
