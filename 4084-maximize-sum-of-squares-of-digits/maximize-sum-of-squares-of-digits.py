class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        nines = sum // 9
        leftover = sum % 9
        zeros = num - nines - (1 if leftover > 0 else 0)
        return "9" * nines + (str(leftover) if leftover > 0 else "") + "0" * zeros