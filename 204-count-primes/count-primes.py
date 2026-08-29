class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        dp = [True] * n
        dp[0] = dp[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if dp[i]:
                dp[i*i : n : i] = [False] * ((n - 1 - i*i) // i + 1)
        return sum(dp)