class Solution(object):
    def numOfStrings(self, patterns, word):
       total = 0
       for pattern in patterns:
        if pattern in word:
            total+=1
       return total
        