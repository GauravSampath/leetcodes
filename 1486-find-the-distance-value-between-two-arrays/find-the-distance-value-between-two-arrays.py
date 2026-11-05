class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
       return sum(d < min(abs(v - u) for u in arr2) for v in arr1)