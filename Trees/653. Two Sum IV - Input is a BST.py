# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        x=[]
        stack=[root]
        while stack:
            node = stack.pop()
            if node:
                x.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        for i in range(len(x)):
            if k-x[i] in x and (k-x[i])!=x[i]:
                return True
