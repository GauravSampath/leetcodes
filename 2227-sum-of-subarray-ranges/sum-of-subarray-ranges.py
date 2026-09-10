class Solution(object):
    def subArrayRanges(self, nums):
        total_sum = 0
        n = len(nums)
        for i in range(n):
            current_min = nums[i]
            current_max = nums[i]
            for j in range(i, n):
                current_min = min(current_min, nums[j])
                current_max = max(current_max, nums[j])
                total_sum += (current_max - current_min)
        return total_sum
