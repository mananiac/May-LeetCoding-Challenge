class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(image, i, j, color, newColor):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != color or image[i][j] == newColor:
                return
            
            image[i][j] = newColor
            dfs(image, i+1, j, color, newColor)
            dfs(image, i, j+1, color, newColor)
            dfs(image, i-1, j, color, newColor)
            dfs(image, i, j-1, color, newColor)
            
        
        dfs(image, sr, sc, image[sr][sc], newColor)
        return image