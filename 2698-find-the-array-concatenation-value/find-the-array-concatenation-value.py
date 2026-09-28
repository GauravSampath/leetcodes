class Solution(object):
    def findTheArrayConcVal(self, nums):
        l = 0
        r = len(nums) - 1
        total = 0
        while l <= r:
            if l == r:
                total += nums[l]
                l += 1
            else:
                total += int(str(nums[l]) + str(nums[r]))
                l += 1
                r -= 1
        return total
    