class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        cnt1 = 0
        cnt2 = 0
        ans = 0
        l = 0
        for r in range(n):
            if(answerKey[r]== "T"):
                cnt1+=1
            else:
                cnt2+=1
            while(min(cnt1,cnt2)>k):
                if(answerKey[l] == "T"):
                    cnt1-=1
                else:
                    cnt2-=1
                l+=1
            ans = max(ans,r-l+1)
        return ans