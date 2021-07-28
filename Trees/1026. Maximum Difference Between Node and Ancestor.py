# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.found=0
        def traverse(root,x):
            if not root:
                return 
            
            x.append(root.val)
            
            if not root.left and not root.right:
                self.found=max(self.found,abs(max(x)-min(x)))
            else:
                traverse(root.left,x)
                traverse(root.right,x)
                
            x.pop()
            
        traverse(root,[])
        return self.found
