class Solution(object):
    def sumOfSquares(self, nums):
        special = 0
        n = len(nums)
        for i in range(n):
            if n % (i+1) == 0:
                special += nums[i] ** 2
        return special