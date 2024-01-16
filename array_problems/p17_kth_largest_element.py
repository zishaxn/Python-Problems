def kth_largest_element(arr,k):
    arr.sort()
    return arr[len(arr)-k]

arr=[1,2,3,4,5]

print(kth_largest_element(arr,2))