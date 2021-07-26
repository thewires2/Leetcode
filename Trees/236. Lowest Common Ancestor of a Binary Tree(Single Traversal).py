# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        
        if root==q or root==p:
            return root
        
        leftlca=self.lowestCommonAncestor(root.left,p,q)
        rightlca=self.lowestCommonAncestor(root.right,p,q)
        
        if leftlca and rightlca:
            return root
        
        return leftlca if leftlca else rightlca
