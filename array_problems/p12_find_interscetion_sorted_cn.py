# https://www.codingninjas.com/studio/problems/intersection-of-2-arrays_1082149
# We need to find intesection {1,2,2,3,4,5,6,7} and {2,2,4,4,5} ans==>> [2, 2, 4, 5]

# APPROACH-1--> BRUTE : TWO FOR LOOPS AND WHEN WE FOUND SET THE SECOND ELEMENT NULL.
#
# APPROACH-2--> OPTIMIZED : HASHMAP
#
# APPROACH-3--> BEST : TWO POINTERS

def findArrayIntersection(list1, list2):
    result1 = []
    l1 = 0
    l2 = 0
    while l1 < len(list1) and l2 < len(list2):
        if list1[l1] > list2[l2]:
            l2 += 1
        elif list1[l1] < list2[l2]:
            l1 += 1
        else:
            result1.append(list1[l1])
            l1+=1
            l2+=1
    return result1



list1 = [1, 2, 2, 3, 4, 5, 6, 7]
list2 = [2, 2, 4, 4, 5]

result = findArrayIntersection(list1, list2)
print(result)
