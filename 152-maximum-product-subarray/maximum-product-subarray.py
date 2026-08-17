class Solution(object):
    def maxProduct(self, nums):
        global_max = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            candidate1 = num * current_max
            candidate2 = num * current_min
            current_max = max(num, candidate1, candidate2)
            current_min = min(num, candidate1, candidate2)
            global_max = max(global_max, current_max)
            
        return global_max  
        