# https://leetcode.com/problems/richest-customer-wealth/
# 1672. Richest Customer Wealth

def find_sum(arr):
    count = 0
    for i in arr:
        count += i
    return count


def richest_customer(arr):
    max_sum = -1
    for i in arr:
        sum = find_sum(i)
        max_sum = max(max_sum, sum)
    return max_sum

accounts = [[1,2,3],[3,2,1]]
result = richest_customer(accounts)
print(result)
