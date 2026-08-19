class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low, high = 1, max(nums)
    
        while low < high:
            mid = (low + high) // 2
            if sum((p + mid - 1) // mid for p in nums) <= threshold:
                high = mid
            else:
                low = mid + 1 
            
        return low

        