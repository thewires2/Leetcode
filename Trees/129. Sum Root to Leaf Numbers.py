# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        def partial_sum(root,partial=0):
            
            if not root:
                return 0
            
            partial = partial*10 + root.val
            
            if root.left==None and root.right==None:
                return partial
            
            return (partial_sum(root.left,partial)+partial_sum(root.right,partial))
        
        return partial_sum(root)
