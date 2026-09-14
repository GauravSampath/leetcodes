class Solution(object):
    def hasSpecialSubstring(self, s, k):
        return any(len(list(g)) == k for _, g in groupby(s))