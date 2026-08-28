class Solution(object):
    def diagonalSum(self, mat):
        total = 0
        n = len(mat)
        for i in range(n):
            total += mat[i][i]
            if i != n - 1 - i:
                total += mat[i][n - 1 - i]
        return total
        