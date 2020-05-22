class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n= len(matrix[0])
        
        count =0
        arr= [[0]*(n+1) for _ in range( m+1)]
        # print(arr)
        for row in range(1,m+1):
            for col in range(1,n+1):
                if matrix[row-1][col-1] ==1:
                    arr[row][col] = 1+min(arr[row][col-1],arr[row-1][col],arr[row-1][col-1])
                    count = count +arr[row][col]
        
        return count