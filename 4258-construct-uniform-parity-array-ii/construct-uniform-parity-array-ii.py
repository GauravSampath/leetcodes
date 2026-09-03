class Solution(object):
    def uniformArray(self, nums1):
        evens_list = [x for x in nums1 if x % 2 == 0]
        odds_list = [x for x in nums1 if x % 2 != 0]
        if not evens_list or not odds_list:
            return True
        min_even = min(evens_list)
        min_odd = min(odds_list)
        return min_odd < min_even


