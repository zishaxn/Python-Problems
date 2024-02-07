# Fibonacci series
def fibo(n):
    if n <= 2:
        return 1
    # print(n)
    return fibo(n - 2) + fibo(n - 1)


print('8th Fibonacci Number is ' + str(fibo(8)))


# -----------------------------------------------------------------------------------------------------
# print nums
def print_nums(n):
    if n == 0:
        return
    print(n)
    print_nums(n - 1)


# print_nums(5)

# -----------------------------------------------------------------------------------------------------
# factorial of a num
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


print('Factorial of first 5 Numbers is ' + str(fact(5)))


# -----------------------------------------------------------------------------------------------------

def sum_of_nums(n):
    if n <= 1:
        return 1
    return n + sum_of_nums(n - 1)


print('Sum of first 5 Numbers is ' + str(sum_of_nums(5)))


# -----------------------------------------------------------------------------------------------------

def num_of_digits(n):
    if int(n / 10) == 0:
        return 1
    return 1 + num_of_digits(int(n / 10))


print('Num of Digits in 452 is ' + str(num_of_digits(45452)))


# -----------------------------------------------------------------------------------------------------

def sum_of_digits(n):
    if int(n / 10) == 0:
        return n
    return int(n % 10) + sum_of_digits(int(n / 10))


print('Sum of Digits in 452 is ' + str(sum_of_digits(452)))


# similarly we can do for multiple.


# -----------------------------------------------------------------------------------------------------

def reverse_number(num):
    if int(num / 10) == 0:
        return num
    return str(int(num % 10)) + str(reverse_number(int(num / 10)))


print(reverse_number(1234))


# -----------------------------------------------------------------------------------------------------

def palindrome_number(num):
    num = str(num)
    return helper(num, 0, len(num) - 1)


def helper(num, start, end):
    if start >= end:
        return True
    if not num[start] == num[end]:
        return False
    return helper(num, start + 1, end - 1);


print('Check if given num if : ' + str(palindrome_number(134321)))


# -----------------------------------------------------------------------------------------------------
def count_zeroes(num):
    if num == 0:
        return 1
    if num < 10:
        return 0

    last_digit = num % 10
    if last_digit == 0:
        return 1 + count_zeroes(num // 10)
    else:
        return count_zeroes(num // 10)


print("No of Zeroes in : " + str(count_zeroes(101020)))
