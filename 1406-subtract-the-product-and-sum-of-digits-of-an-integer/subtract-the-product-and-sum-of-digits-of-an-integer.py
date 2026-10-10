class Solution(object):
    def subtractProductAndSum(self, n):
       import math
       digits = [int(d) for d in str(n)]
       s = sum(digits)
       p = 1
       for d in digits:
            p *= d
            result = p - s
       return result