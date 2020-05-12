class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        Manan =0
        for i in nums:
            Manan = Manan^ i
        return Manan
            