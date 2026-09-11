class Solution(object):
    def numberOfSubarrays(self, nums, k):
       l = 0 
       ans = 0
       n = len(nums)
       odd_count = 0
       prefix_evens = 0
       for r in range(n):
        if nums[r] % 2 == 1:
            odd_count += 1
        while odd_count > k:
            if nums[l] % 2 == 1:
                odd_count -= 1
            l += 1
            prefix_evens = 0 
        if odd_count == k:
            while nums[l] % 2 == 0:
                prefix_evens += 1
                l += 1
            ans += (prefix_evens + 1)
       return ans