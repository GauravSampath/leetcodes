class Solution(object):
    def isIsomorphic(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))
        