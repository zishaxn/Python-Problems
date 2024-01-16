# You have been given an empty array(ARR) and its size N.
# The only input taken from the user will be N and you need not worry about the array.
# Your task is to populate the array using the integer values in the range 1 to N(both inclusive)
# in the order - 1,3,5,.......,6,4,2.

# Sample Input 1 :
# 6
# Sample Output 1 :
# 1 3 5 6 4 2
# https://www.codingninjas.com/studio/problems/arrange-numbers-in-array_4353

def arrange_numbers(arr):
    start = 0
    end = len(arr)-1
    i = 1
    while start <= end:
        if i % 2 != 0:
            arr[start] = i
            start += 1
        else:
            arr[end] = i
            end -= 1
        i += 1


arr = [0]*9

arrange_numbers(arr)
print(arr)


