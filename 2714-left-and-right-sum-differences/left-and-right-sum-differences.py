class Solution(object):
    def leftRightDifference(self, nums):
        return [abs(sum(nums[:i]) - sum(nums[i+1:])) for i in range(len(nums))]