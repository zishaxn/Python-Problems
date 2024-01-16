
# //https://leetcode.com/problems/move-zeroes/
def move_zeroes(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < len(arr):
        arr[count] = 0
        count += 1


nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)
