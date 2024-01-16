# https://www.geeksforgeeks.org/problems/find-unique-element2632/1


# To use hashmaps in python we can directly create it using "{}" and we can directly assign any key with a pair
# using map[key]=value.
def find_unique(arr, mul):
    frequency_map = {}
    for key in arr:
        if key in frequency_map:
            frequency_map[key] += 1
        else:
            frequency_map[key] = 1
    for key in arr:
        if key in frequency_map and frequency_map[key] % mul != 0:
            return key
    return -1


arr = [6, 2, 5, 2, 2, 6, 6]
mul = 3

result = find_unique(arr, mul)
print("Unique element:", result)
