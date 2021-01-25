# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        x=[]
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                x.append([node.val,abs(node.val-target)])
                stack.append(node.left)
                stack.append(node.right)
        x.sort(key=lambda a:a[1])
        return x[0][0]
