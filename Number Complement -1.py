class Solution:
    def findComplement(self, num: int) -> int:
        # num = int(input())

        num = bin(num)
        arr1=""
        
        for i in range(2,len(num)):
            if num[i]== "1":
                arr1=arr1+"0"
            if num[i]== "0":
                arr1=arr1+"1"
        
        return (int(arr1,2))