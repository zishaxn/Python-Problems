
# https://leetcode.com/problems/find-the-duplicate-number/

def find_duplicate(arr):
    freq_map = {}
    for key in arr:
        if key in freq_map:
            return key
        else:
            freq_map[key] = 1
    return -1


def find_duplicate_h_t(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]

        if slow == fast:
            break
    fast = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow


list = [1, 2, 2, 3, 5, 4]
result = find_duplicate_h_t(list)
print(result)
