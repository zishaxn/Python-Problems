import math


# Problem 1 : Sum of List Elements:

def sum_list(arr):
    sum_arr = 0
    for i in arr:
        sum_arr += i
    return sum_arr


print('Answer 1', end=' ')
my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))


# -----------------------------------------------------------------------------------

# Problem 2 :Maximum of Three Numbers:
def max_of_nums(num, num2, num3):
    return max(num, num2, num3)


print('Answer 2', end=' ')
print(max_of_nums(-5, 0, -9))


# -----------------------------------------------------------------------------------

# Problem 3 : Factorial Calculation:
def calculate_fact(num):
    # fact = 1
    # while num >= 1:
    #     fact = num * fact
    #     num -= 1
    # return fact
    return math.factorial(num)


print('Answer 3', end=' ')
print(calculate_fact(5))


# -----------------------------------------------------------------------------------

# Problem 4 : Reverse a String:
def reverse_string(string):
    return string[::-1]


print('Answer 4', end=' ')
print(reverse_string('Hello World!'))


# -----------------------------------------------------------------------------------

# Problem 5 : count vowels
def count_vowels(string):
    count = 0
    for i in string:
        if i == 'a' or i == 'e' or i == 'o' or i == 'u' or i == 'i':
            count += 1
    return count


print('Answer 5', end=' ')
print(count_vowels('The joyous yellow flowers bloomed beautifully in the peaceful garden.'))


# -----------------------------------------------------------------------------------

# Problem 6 : Intersection of Lists:

def intersection_of_lists(list1, list2):
    # result = []
    # for i in list1:
    #     for j in range(len(list2)):
    #         if i == list2[j]:
    #             result.append(i)
    #             list2[j] = -1
    # return result

    list1 = set(list1)
    list2 = set(list2)

    return list1.intersection(list2)


list1 = [1, 2, 3]
list2 = [3, 5]

print('Answer 6', end=' ')
print(intersection_of_lists(list1, list2))


# -----------------------------------------------------------------------------------

# Problem 7 : Remove Duplicates:
# Implement a function that takes a list as input and returns a new list with duplicate elements removed.

def remove_duplicates(list_input):
    # list_input = set(list_input)
    # list_input = list(list_input)
    # return list_input
    return set(list_input)


list_given = [1, 5, 2, 3, 1, 4, 6, 2]
print('Answer 7', end=' ')
print(remove_duplicates(list_given))


# -----------------------------------------------------------------------------------

# Problem 8 : Check Palindrome:
# Create a function that takes a string as input and returns True if it is a palindrome
# (reads the same backward as forward), and False otherwise.

def check_palindrome(string_input):
    start = 0
    end = len(string_input) - 1
    while start <= end:
        if not (string_input[start] == string_input[end]):
            return False
        start += 1
        end -= 1
    return True


print('Answer 8', end=' ')
print(check_palindrome('MALYALAM'))


# -----------------------------------------------------------------------------------

# Problem 9 : Power of a Number:
# Write a function that takes two numbers as arguments, base and exponent,
# and returns the result of raising the base to the power of the exponent.

def power_of_num(base, exponent):
    return math.pow(base, exponent)


print('Answer 9', end=' ')
print(power_of_num(5, 2))


# -----------------------------------------------------------------------------------

# Problem 10 : Fibonacci Sequence: Implement a function that generates the first n numbers in the Fibonacci sequence,
# where each number is the sum of the two preceding ones.

def fibonacci_numbers(num):
    list_result = []
    first = 0
    second = 1
    list_result.append(first)
    list_result.append(second)
    # print(first, end=' ')
    # print(second, end=' ')
    while num-2 >= 0:
        curr_sum = first + second
        # print(curr_sum, end=' ')
        list_result.append(curr_sum)
        first = second
        second = curr_sum
        num -= 1
    return list_result

print('Answer 10', end=' ')
print(fibonacci_numbers(5))
