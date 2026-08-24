class Solution(object):
    def maxDepth(self, s):
       ans = 0
       depth = 0
       for c in s:
        if c=="(":
            depth+=1
            ans = max(ans,depth)
        elif c == ")":
            depth-=1
       return ans




        