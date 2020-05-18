from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lens,lenp=len(s),len(p)
        arr=[]
        if lenp>lens:
            return arr
        else: 
            
            s_count,p_count = Counter(),Counter(p)
            
            for i in range(len(s)):
                
                s_count[s[i]]=s_count[s[i]]+1
                    
                if i>= lenp :
                    
                    if s_count[s[i-lenp]] == 1:
                        
                        del s_count[s[i-lenp]]
                    else:
                        s_count[s[i-lenp]] -=1
                if s_count == p_count:
                    arr.append(i-lenp+1)
            return arr
                    