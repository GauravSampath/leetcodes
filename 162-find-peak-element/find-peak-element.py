class Solution(object):
    def findPeakElement(self, nums):
       for i,n in enumerate(nums):
        if n == max(nums):
            return i
        