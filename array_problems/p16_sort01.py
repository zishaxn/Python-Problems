def sort012(nums):
    zero = one = 0

    for i in nums:
        if i == 0:
            zero += 1
        elif i == 1:
            one += 1

    i = 0
    for i in range(zero):
        nums[i] = 0

    for i in range(zero, zero + one):
        nums[i] = 1

    for i in range(zero + one, len(nums)):
        nums[i] = 2


arr = [0,2,1,1,0,0,0,2,1,1]
sort012(arr)
print(arr)