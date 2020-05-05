class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        if len(ransomNote) > len(magazine):
            return False
        for i in magazine:
            if i in d:
                d[i]= d[i] +1
            else:
                d[i] = 1
        for i in ransomNote:
            
            if i not in d:
                return False
            elif d[i] == 0:
                return False
            elif i in d:
                d[i]-=1
        return True       