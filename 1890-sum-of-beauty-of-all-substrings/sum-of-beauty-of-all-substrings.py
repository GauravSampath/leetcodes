class Solution(object):
    def beautySum(self, s):
        total_beauty = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1
                counts = freq.values()
                minF = min(counts)
                maxF = max(counts)
                total_beauty+=(maxF-minF)
        return total_beauty

        

        