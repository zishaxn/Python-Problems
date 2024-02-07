def searchRange(self, nums, target):
    ans = [-1, -1]
    ans[0] = self.search(nums, target, True)
    ans[1] = self.search(nums, target, False)
    return ans


def search(arr, target, isFirst):
    ans = -1
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            ans = mid
            if isFirst:
                end = mid - 1
            else:
                start = mid + 1
    return ans
