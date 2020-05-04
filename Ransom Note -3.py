class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for item in ransomNote:
            if not item in magazine:
                return False
            magazine = magazine.replace(item, "", 1)
        return True