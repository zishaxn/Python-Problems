# https://leetcode.com/problems/intersection-of-two-arrays/
# In this question we required to only return numbers that are common in both and they should occur only once,
#  It means that if l1 = 1,2,2,3,4,6 and l2 = 1,2,2,5 then it should return [1,2] not [1,2,2]

def intersection(nums1, nums2):
    ans = []
    freq_map = {}
    for i in nums1:
        freq_map[i] = 1
    for i in nums2:
        if i in freq_map:
            ans.append(i)
            freq_map.pop(i)
    return ans;


nums1 = [4,9,4,5]
nums2 = [9,4,9,8,4]

result = intersection(nums1, nums2)
print(result)
