# https://www.codingninjas.com/studio/problems/swap-alternate_624941
def swap_alternate(arr):
    for i in range(0, len(arr) - 1, 2):
        temp = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = temp


arr = [1, 2, 3, 4, 5, 6, 7]
swap_alternate(arr)
print(arr)
