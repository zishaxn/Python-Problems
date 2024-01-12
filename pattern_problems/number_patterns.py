

# 1
# 2 2
# 3 3 3
# 4 4 4 4

def pattern1(num):
    for row in range(1, num + 1):
        for col in range(1, row + 1):
            print(row, end=' ')
        print()


# pattern1(4)

# ----------------------------------------------------------------------------------


# 1
# 2 1
# 3 2 1
# 4 3 2 1

def pattern2(num):
    for row in range(1, num + 1):
        for col in range(row, 0, -1):
            print(col, end=' ')
        print()


# pattern2(4)

# ----------------------------------------------------------------------------------

# 1
# 2 3
# 4 5 6
# 7 8 9 10

def pattern3(num):
    i = 0
    for row in range(1, num + 1):
        for col in range(1, row + 1):
            i += 1
            print(i, end=' ')
        print()


# pattern3(4)

# ----------------------------------------------------------------------------------

# 1 2 3 4 4 3 2 1
# 1 2 3 * * 3 2 1
# 1 2 * * * * 2 1
# 1 * * * * * * 1

def pattern4(nums):
    for row in range(0, nums):
        for cols in range(1, nums - row + 1):
            print(cols, end=' ')
        stars = 2 * row
        for star in range(0, stars):
            print('*', end=' ')
        for cols in range(nums - row, 0, -1):
            print(cols, end=' ')
        print()


# pattern4(4)

# ----------------------------------------------------------------------------------

# 4 5 6 7
# 3 4 5 6
# 2 3 4 5
# 1 2 3 4

def pattern5(nums):
    for row in range(nums, 0, -1):
        num = row
        for col in range(0, nums):
            print(num, end=' ')
            num+=1
        print()

# pattern5(4)

# ----------------------------------------------------------------------------------

#       1
#     2 3 2
#   3 4 5 4 3
# 4 5 6 7 6 5 4


def pattern6(nums):
    for row in range(1,nums+1):
        spaces = nums-row;
        for space in range(1,spaces+1):
            print(' ',end=' ')
        num = row
        for col in range(0,row):
            print(num,end=' ')
            num+=1
        rev_nums = num-2
        for rev_num in range(0,row-1):
            print(rev_nums,end=' ')
            rev_nums-=1
        print()

pattern6(4)

