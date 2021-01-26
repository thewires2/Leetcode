# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        x=[]
        s=0
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                x.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        x.sort()
        for i in range(1,len(x)):
            if s==0:
                s=abs(x[i]-x[i-1])
            else:
                s=min(s,x[i]-x[i-1])
        return s
