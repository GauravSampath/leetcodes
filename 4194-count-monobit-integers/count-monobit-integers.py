class Solution(object):
    def countMonobit(self, n):
       return (n + 1).bit_length()
        