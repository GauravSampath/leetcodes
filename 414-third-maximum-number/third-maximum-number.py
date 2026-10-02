class Solution(object):
    def thirdMax(self, nums):
        n = set(nums)
        if len(n) < 3:
            return max(nums)
        return sorted(n)[-3]
