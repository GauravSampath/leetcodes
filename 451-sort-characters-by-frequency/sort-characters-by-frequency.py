class Solution(object):
    def frequencySort(self, s):
        from collections import Counter
        cnt = Counter(s)
        return "".join(char * count for char, count in cnt.most_common())


        