class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        total = 0
        for hour in hours:
            if hour >= target:
                total+=1
        return total