class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        if k == n:
            return total_sum
        l = 0 
        max_score = 0
        current_window_sum = 0
        window_size = n - k
        for r in range(n):
            current_window_sum += cardPoints[r]
            if r - l + 1 == window_size:
                max_score = max(max_score, total_sum - current_window_sum)
                current_window_sum -= cardPoints[l]
                l += 1
        return max_score

       
