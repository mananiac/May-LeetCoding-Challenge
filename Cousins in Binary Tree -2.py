# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        arr = [[0, 0] for _ in range(101)]        
        def traverse(r, depth, pv):
            if not r: return 
            arr[r.val] = [depth, pv]
            traverse(r.left, depth + 1, r.val)
            traverse(r.right, depth + 1, r.val)            
        
        traverse(root, 0, -1)
        return arr[x][0] == arr[y][0] and arr[x][1] != arr[y][1]
        