class Solution(object):
    def hasTrailingZeros(self, nums):
        return sum(num%2==0 for num in nums) > 1