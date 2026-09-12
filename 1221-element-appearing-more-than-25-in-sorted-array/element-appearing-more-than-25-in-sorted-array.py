class Solution(object):
    def findSpecialInteger(self, arr):
      return next(x for x in set(arr) if arr.count(x) > len(arr) / 4)
