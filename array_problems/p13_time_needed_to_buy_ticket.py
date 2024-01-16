def time_needed_to_buy_tickets(arr, n):
    person = arr[n]
    time = 0
    for i in range(len(arr)):
        if i <= n:
            time += min(person, arr[i])
        else:
            time += min(person - 1, arr[i])
    return time


arr = [2, 3, 5, 2, 4, 6, 1]
n = 2
result = time_needed_to_buy_tickets(arr, n)
print(result)
