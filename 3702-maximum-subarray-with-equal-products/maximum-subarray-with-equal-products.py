class Solution:
    def maxLength(self, nums: List[int]) -> int:
        return max(
        j - i
        for i in range(len(nums))
        for j in range(i + 1, len(nums) + 1)
        if math.prod(nums[i:j]) == math.lcm(*nums[i:j]) * math.gcd(*nums[i:j])
    ) 