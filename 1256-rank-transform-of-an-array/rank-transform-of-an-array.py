class Solution(object):
    def arrayRankTransform(self, arr):
        d = {}
        ind = 1
        for i in sorted(set(arr)):
            d[i] = ind
            ind += 1
        return [d[i] for i in arr]