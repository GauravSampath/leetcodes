class Solution(object):
    def minElement(self, nums):
         return min(sum(int(digit) for digit in str(num)) for num in nums)
        