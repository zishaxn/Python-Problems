def binary_search(nums, target):
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

    return -1  # Return -1 if the target is not found in the array

arr = [15, 16, 17, 18, 19, 20]
target = 18
print(binary_search(arr, target))
