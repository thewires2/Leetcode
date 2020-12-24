# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        self.x=[]
        def lone(root):
            if root:
                if root.left and not root.right:
                    self.x.append(root.left.val)
                    lone(root.left)
                elif root.right and not root.left:
                    self.x.append(root.right.val)
                    lone(root.right)
                else:
                    lone(root.left)
                    lone(root.right)
        lone(root)
        return self.x
    
