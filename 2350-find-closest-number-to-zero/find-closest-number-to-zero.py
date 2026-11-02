class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        return min(nums, key=lambda x: (abs(x), -x))
