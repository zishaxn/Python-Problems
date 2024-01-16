def merge(nums1, m, nums2, n):
    n1 = m - 1
    n2 = n - 1
    k = m + n - 1
    while n1 >= 0 and n2 >= 0:
        if nums1[n1] > nums2[n2]:
            nums1[k] = nums1[n1]
            k -= 1
            n1 -= 1
        else:
            nums1[k] = nums2[n2]
            k -= 1
            n2 -= 1
    while n2 >= 0:
        nums1[k] = nums2[n2]
        k -= 1
        n2 -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
