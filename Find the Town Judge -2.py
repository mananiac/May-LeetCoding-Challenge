
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        a=[]
        b=[]
        c=[]
        count = 0
        if N==1:
            return 1
        for i in range(len(trust)):
            a.append(trust[i][0])
            b.append(trust[i][1])
        # a.sort()
        for i in range(len(b)):
            if b[i] not in a:
                c.append(b[i])
        print(a,b,c)
        for i in range(len(c)):
            count=1
            for j in range(1,len(c)):
                if c[i] == c[j]:
                    count+=1
            print(count)
            if count == N-1:
                return c[i]
        return -1
                
        
