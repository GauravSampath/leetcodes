class Solution(object):
    def minAddToMakeValid(self, s):
        score = 0
        depth = 0
        for i in range(len(s)):
            if s[i] == "(":
                depth+=1
            elif s[i] == ")":
                if depth > 0:
                    depth -= 1
                elif depth == 0:
                    score +=1
        return score + depth
        