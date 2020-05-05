class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range (len(s)):
            if (s[i] in s[i+1:]) or (s[i] in s[:i]):
                continue
            elif (len(s)==2)  and s[0]==s[1]:
                return -1
            elif (s[i] not in s[i+1:]) or (s[i] not in s[:i]):
                return i
            
        return -1