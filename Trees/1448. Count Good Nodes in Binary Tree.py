# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.x=0
        
        def traverse(root,y):
            if not root: return
            
            y.append(root.val)
            
            if root.val==max(y):
                self.x+=1
                
            traverse(root.left,y)
            traverse(root.right,y)
            
            y.pop()
        traverse(root,[])
        return self.x
