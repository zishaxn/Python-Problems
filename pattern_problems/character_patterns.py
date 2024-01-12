def pattern1(nums):
    for row in range(0, nums):
        char = chr(ord('A')+row)
        for col in range(0, row + 1):
            print(char, end=' ')
        print()


pattern1(4)
