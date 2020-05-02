class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = list(J)
        s = list(S)
        count = 0
        for i in j:
            for k in s:
                if i == k:
                    count+=1
        return count            