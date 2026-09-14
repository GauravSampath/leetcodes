class Solution(object):
    def hasSpecialSubstring(self, s, k):
        return any(sum(1 for _ in g) == k for _, g in groupby(s))
