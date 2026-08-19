class Solution(object):
    def search(self, nums, target):
      for i,n in enumerate(nums):
        if n == target:
            return True
      return False
        