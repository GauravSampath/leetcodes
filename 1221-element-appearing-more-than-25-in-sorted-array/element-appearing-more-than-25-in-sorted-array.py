class Solution(object):
    def findSpecialInteger(self, arr):
     return Counter(arr).most_common(1)[0][0]
