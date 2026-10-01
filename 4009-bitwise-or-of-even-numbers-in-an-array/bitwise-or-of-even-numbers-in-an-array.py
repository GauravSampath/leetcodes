class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        result = 0
        for num in nums:
            if num % 2 == 0:
                result |= num
        return result