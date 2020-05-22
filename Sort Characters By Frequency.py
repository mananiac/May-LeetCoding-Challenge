class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        r=""
        for i in s:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        s=sorted(d,key = lambda x: d[x],reverse = True)
        
        for i in s:
            r=r+i*d[i]
        return r