def is_sorted(arr):
    return helper(arr, 0, len(arr) - 1)

def helper(arr, si, ei):
    if si >= ei:
        return True

    if arr[si] < arr[ei]:
        return helper(arr, si + 1, ei - 1)
    else:
        return False


def helper2(arr,index):
    if index==len(arr)-1:
        return True
    return arr[index]<arr[index+1] and helper2(arr,index+1);
# Example usage:
arr = [1, 2, 3,2, 4, 5]

result = is_sorted(arr)
print(result)  # Output: True
