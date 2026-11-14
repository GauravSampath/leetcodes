class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        best = float("inf")
        n = len(nums)
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                length = j - i + 1
                if l <= length <= r and curr > 0:
                    best = min(best, curr)     
        if best == float("inf"):
            return -1
        return best