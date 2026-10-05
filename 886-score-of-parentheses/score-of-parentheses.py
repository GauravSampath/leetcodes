class Solution(object):
    def scoreOfParentheses(self, s):
       score = 0
       depth = 0
       for i in range(len(s)):
        if s[i] == "(":
            depth += 1
        elif s[i] == ")":
            depth -= 1
            if s[i-1] == "(":
                score += 2 ** depth
       return score