class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+10):
            prod = 1
            temp = i
            while temp >0:
             prod *= temp % 10
             temp //= 10

            if prod % t == 0:
             return i
