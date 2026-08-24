class Solution(object):
    def beautySum(self, s):
        ans = 0
        for i in range(len(s)):
            cnt = [0] * 26
            for j in range(i, len(s)):
                cnt[ord(s[j]) - 97] += 1
                vals = [f for f in cnt if f]
                ans += max(vals) - min(vals)
        return ans

        