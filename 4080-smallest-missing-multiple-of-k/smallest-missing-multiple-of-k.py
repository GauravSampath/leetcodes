class Solution(object):
    def missingMultiple(self, nums, k):
       num_set = set(nums)
       current_multiple = k
       while current_multiple in num_set:
        current_multiple += k
       return current_multiple