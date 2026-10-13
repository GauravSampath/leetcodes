class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = sorted(x * x for x in nums)
        n = len(squares)
        split_idx = n // 2
        negative_part = sum(squares[:split_idx])
        positive_part = sum(squares[split_idx:])
        return positive_part - negative_part