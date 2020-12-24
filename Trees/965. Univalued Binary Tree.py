# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root:
            self.k=root.val
            self.x=[]
            self.x.append(root.val)
        else:
            return True
        def abc(root):
            if root:
                if root.left:
                    self.x.append(root.left.val)
                    abc(root.left)
                if root.right:
                    self.x.append(root.right.val)
                    abc(root.right)
        abc(root)
        print(len(self.x))
        if len(set(self.x))!=1:
            return False
        return True
            

                
                
            
