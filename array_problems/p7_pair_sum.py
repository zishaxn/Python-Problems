def pair_sum(arr, s):
    result = []
    freq_map = {}
    for num in arr:
        complement = s - num
        if complement in freq_map and freq_map[complement] > 0:
            pair = [min(num, complement), max(num, complement)]
            result.append(pair)
        else:
            freq_map[num] = (freq_map.get(num, 0) + 1)
            print(freq_map[num])

    return result


# Sample Input 1
arr1 = [1, 1,2, 3, 4, 5]
s1 = 5
result1 = pair_sum(arr1, s1)
print("Sample Output 1:")
for pair in result1:
    print(pair[0], pair[1])

# Sample Input 2
arr2 = [2, -3, 3, 3, -2]
s2 = 0
result2 = pair_sum(arr2, s2)
print("Sample Output 2:")
for pair in result2:
    print(pair[0], pair[1])

# Additional Test Case 1
arr3 = [3, 1, 4, 2, 5]
s3 = 6
result3 = pair_sum(arr3, s3)
print("Additional Test Case 3:")
for pair in result3:
    print(pair[0], pair[1])

# Additional Test Case 2
arr4 = [-1, 0, 1, 2, -1, -4]
s4 = 0
result4 = pair_sum(arr4, s4)
print("Additional Test Case 4:")
for pair in result4:
    print(pair[0], pair[1])
