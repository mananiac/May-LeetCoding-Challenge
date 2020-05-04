class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_r=Counter(ransomNote)
        count_m=Counter(magazine)
        for char in count_r:
            if count_r[char]>count_m[char]:
                return False
        return True