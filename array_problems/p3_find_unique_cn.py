# https://www.codingninjas.com/studio/problems/find-unique_625159


# we know that each element will be having exactly one duplicate element and not more than that and there
# will be a unique num
def find_unique(arr):
    result = 0
    for i in arr:
        result=result^i
    return result;

arr = [1,2,3,3,2,1,4]
result = find_unique(arr)
print(result)
