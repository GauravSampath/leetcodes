class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        prefixMax = [0] * n
        prefixMax[0] = nums[0]
        suffixMin = [0] * n
        suffixMin[n-1] = nums[n-1]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i-1], nums[i])
        for i in range(n-2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i+1])
        for i in range(n):
            score = prefixMax[i] - suffixMin[i]
            if score <= k:
                return i
        return -1

        