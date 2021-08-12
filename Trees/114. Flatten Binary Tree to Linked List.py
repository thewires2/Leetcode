# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        
        def shift(node):
            
            if not node: return None
            if not node.left and not node.right: return node
            
            leftTail=shift(node.left)
            rightTail=shift(node.right)
            
            if leftTail:
                leftTail.right=node.right
                node.right=node.left
                node.left=None
            return rightTail if rightTail else leftTail
                
        shift(root)

                
                
