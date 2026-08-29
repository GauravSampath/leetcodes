class Solution(object):
    def subsets(self, nums):
       return [list(s) for r in range(len(nums) + 1) for s in __import__('itertools').combinations(nums, r)]
        