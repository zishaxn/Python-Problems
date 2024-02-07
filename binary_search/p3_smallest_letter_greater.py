# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# ceiling in chars

def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] == target:
            return letters[mid]
        elif letters[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return letters[left % len(letters)]


letters = ["c", "f", "j"]
target = "a"
print(nextGreatestLetter(letters, target))
