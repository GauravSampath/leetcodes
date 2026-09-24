class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            if i == sum(int(digit) for digit in str(nums[i])):
                return i
        return -1