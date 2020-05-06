class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max= 0
        ele={}
        for i in nums:
            if i in ele:
                ele[i]+=1
            else:
                ele[i] =1
        print(ele)
        for i in ele:
            if ele[i]>(len(nums)//2):
                return i