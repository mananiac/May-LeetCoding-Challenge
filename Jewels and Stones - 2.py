class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jSet = set(J)
        
        count = 0
        for i in S:
            
            if i in jSet:
                count+=1
        return count            