class Solution(object):
    def checkDivisibility(self, n):
        chill=str(n)
        prod=1
        sui=0
        for i in chill:
            prod*=int(i)
            sui+=int(i)   
        return n%(prod+sui)==0   