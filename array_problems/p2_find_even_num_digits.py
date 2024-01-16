# Given an array nums of integers, determine how many numbers in the array have an even number of digits.
#
# Example:
#
# Input: nums = [12, 345, 2, 6, 7896]
#
# Output: 2
#
# Explanation: Numbers 12 and 7896 have an even number of digits.
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

def find_even_digits(arr):
    count = 0
    for i in arr:
        if is_even(i):
            count += 1
    return count


def is_even(num):
    count = 0
    while num > 0:
        num = int(num / 10)
        count += 1
    return count % 2 == 0


arr = [12, 345, 2, 16, 7896]
result = find_even_digits(arr)
print(result)
