
        
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        btree_dic = {}
        
        def traverse (root,parent =None ,depth =0):
            if root and (x not in btree_dic or y not in btree_dic ):
                btree_dic[root.val] = (depth,parent)
                traverse(root.left,root,depth+1)
                # print(btree_dic)
                traverse(root.right,root,depth+1)
                # print(btree_dic)

        traverse(root)
        return btree_dic[x][0] == btree_dic[y][0] and btree_dic[x][1] != btree_dic[y][1]
        
        