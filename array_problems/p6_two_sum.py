def two_sum(arr, target):
    freq_map = {}
    ans = [0]*2
    for i in range(len(arr)):
        curr_element = target-arr[i]
        if curr_element in freq_map:
            ans[0]=i
            ans[1]=freq_map[curr_element]
        else:
            freq_map[arr[i]]=i
    return ans

arr = [1,3,2,8,12,7]
target = 9

result = two_sum(arr, target)
print(result)
