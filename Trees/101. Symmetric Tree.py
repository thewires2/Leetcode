# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def sym(left,right):
            if not left and not right:
                return True
            try:
                return (left.val==right.val) and sym(left.left,right.right) and sym(left.right,right.left)
            except:
                return False
        
        return sym(root.left,root.right)
