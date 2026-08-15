class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)       
        result = set()
        counts = {}
    
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
            if counts[num] > (n // 3):
                result.add(num)
            
        return list(result)

        