class Solution(object):
    def largestEven(self, s):
       idx = s.rfind('2')
       if idx == -1:
        return ""
       return s[:idx + 1]



        