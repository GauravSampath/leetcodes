class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        mini = [0] * n

        mint = float('inf')
        for i in range(n - 1, -1, -1):
            if nums[i] < mint:
                mint = nums[i]
            mini[i] = mint

        maxt = 0
        for i in range(n):
            if nums[i] > maxt:
                maxt = nums[i]
            if maxt - mini[i] <= k:
                return i

        return -1