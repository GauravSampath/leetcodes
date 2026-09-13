class Solution(object):
    def numberOfSubstrings(self, s):
        l = 0
        ans = 0
        Counter = {'a': 0, 'b': 0, 'c': 0}
        for r in range(len(s)):
           Counter[s[r]] +=1
           while Counter['a'] > 0 and  Counter['b'] > 0 and  Counter['c'] > 0:
            Counter[s[l]] -= 1
            l+=1
            ans += len(s)-r
        return ans
