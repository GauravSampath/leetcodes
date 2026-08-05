class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        z = 0
        o = 0
        t = 0
        for i in range(n):
            if nums[i] == 0:
                z+=1
            elif nums[i] == 1:
                o +=1
            else:
                t+=1
            
        nums[:] =[0] * z +[1] * o +[2] * t
        