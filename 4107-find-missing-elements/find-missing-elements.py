class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l = []
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(nums[i]+1, nums[i+1]):
                l.append(j)
        return l