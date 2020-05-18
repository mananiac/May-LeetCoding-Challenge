class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p,s=s1,s2
        lens,lenp=len(s),len(p)
        
        if lenp>lens:
            return False
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
                    return True
            
            return False
           