class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        lst = []
        indices = [i for i, num in enumerate(nums) if num == x]
        for q in queries:
            if q <= len(indices):
                lst.append(indices[q - 1]) 
            else:
                lst.append(-1)
        return lst
        