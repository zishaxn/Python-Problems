def findTriplets(arr, n, target):
    result = []
    arr.sort()

    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]

            if curr_sum == target:
                ans = [arr[i], arr[left], arr[right]]
                result.append(ans)

                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

    return result


arr = [1, 2, 3, 1, 2, 3]
ans = findTriplets(arr, len(arr), 6)
print(ans)
