class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)
        if n <= 2:
            return n
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        from_front = j + 1
        from_back = n - i
        from_both = (i + 1) + (n - j)
        return min(from_front, from_back, from_both)
        