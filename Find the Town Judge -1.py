
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N-1:
            returm -1
        a=[0]*(N+1)
        for i,j in trust:
            a[i]-=1
            a[j]+=1
        for i,score in enumerate (a[1:],1):
            if score==(N-1):
                return i
        return -1
        
        
