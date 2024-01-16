def missing_numbers(arr):
    n = len(arr)
    expected_sum = (n*(n+1))/2
    sum = 0
    for i in arr:
        sum+=i;
    return expected_sum-sum

arr = [0,1,3]
print(missing_numbers(arr))