# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
# floor of number
# // find the biggest number that is equal to or less than the given number.
def findFloor(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right


arr = [1, 2, 8, 10, 11, 12, 19]
target = 5
print(findFloor(arr, target))
