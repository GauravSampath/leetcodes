class Solution(object):
    def intersect(self, nums1, nums2):
         C = collections.Counter
         return list((C(nums1) & C(nums2)).elements())