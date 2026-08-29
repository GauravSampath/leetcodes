class Solution(object):
    def minBitFlips(self, start, goal):
        xor_result = start ^ goal
        return bin(xor_result).count("1")
        