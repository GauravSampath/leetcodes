
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = n

                for d in range(1, length):
                    if length % d == 0:
                        count = 0

                        for x in range(d):
                            left = i + x
                            right = j - d + 1 + x

                            while left < right:
                                if s[left] != s[right]:
                                    count += 1

                                left += d
                                right -= d

                        best = min(best, count)

                cost[i][j] = best

        dp = [[n] * (k + 1) for _ in range(n + 1)]

        dp[n][0] = 0

        for i in range(n - 1, -1, -1):
            for parts in range(1, k + 1):
                for j in range(i + 1, n):
                    dp[i][parts] = min(
                        dp[i][parts],
                        cost[i][j] + dp[j + 1][parts - 1]
                    )

        return dp[0][k]