def linear_search(arr, target):
    return linear_search_helper(arr, target, 0)


def linear_search_helper(arr, target, index):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    else:
        return linear_search_helper(arr, target, index + 1)


# arr = [1, 2, 3, 2, 4, 5, 2]
# target = 3


# print()


# -------------------------------------------------------------------------------------------------------------

def find_all_ocurrences(arr, target):
    ans = []
    return find_all_occurrences_helper(arr, target, 0, ans)


def find_all_occurrences_helper(arr, target, index, ans):
    if index == len(arr):
        return ans

    if arr[index] == target:
        ans.append(index)
    return find_all_occurrences_helper(arr, target, index + 1, ans) 


arr = [1, 2, 3, 2, 4, 5, 2]
target = 2

print(find_all_ocurrences(arr, target))
