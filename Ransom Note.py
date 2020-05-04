class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a,b=sorted(ransomNote),sorted(magazine)
        for i in range(len(a)):
        # for j in range(i,len(b)):
            if a[i] in b[i:]:
                y=b.index(a[i])
                b[y]=-1
            else:
                return (False)

        return (True)