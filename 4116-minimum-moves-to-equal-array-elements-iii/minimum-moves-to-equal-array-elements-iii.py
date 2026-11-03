class Solution:
    def minMoves(self, nums: List[int]) -> int:
       n = max(nums)
       total = 0
       for i in range(len(nums)):
            total+=n - nums[i]
       return total