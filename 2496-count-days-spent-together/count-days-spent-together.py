YDAY = [0,0] + [*accumulate([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])]
class Solution:
    def countDaysTogether(self, aAlice: str, lAlice: str, aBob: str, lBob: str) -> int:
        def nDay(date: str):
            mm,dd = list(map(int,date.split('-')))
            return  YDAY[mm] + dd
        return  max(0, min(nDay(lAlice),nDay(lBob)) -max(nDay(aAlice),nDay(aBob)) +1)
        