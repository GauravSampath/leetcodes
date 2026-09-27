class Solution(object):
    def reverseParentheses(self, s):
        while ')' in s:
            r = s.find(')')
            l = s.rfind('(', 0, r)
            s = s[:l] + s[l+1:r][::-1] + s[r+1:]
        return s