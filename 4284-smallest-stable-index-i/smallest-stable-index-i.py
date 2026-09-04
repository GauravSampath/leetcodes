class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        for i in range(0, n):
            a = max(nums[:i+1])
            b = min(nums[i:])
            score = a-b
            if score <= k:
             return i
        return -1

        