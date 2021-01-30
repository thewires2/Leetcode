# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        
        def ite(root):
            x=[]
            stack=[root]
            while stack:
                node=stack.pop()
                if node:
                    x.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            return x
        y=ite(root1)
        z=ite(root2)
        for i in y:
            if target-i in z:
                return True
