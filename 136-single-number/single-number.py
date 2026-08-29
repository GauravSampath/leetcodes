class Solution(object):
    def singleNumber(self, nums):
      answer = 0
      for num in nums:
        answer ^= num
      return answer

        