# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        x=[]
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                x.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        print(sorted(x))
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                node.val+=sum([i for i in x if i>node.val])
                stack.append(node.left)
                stack.append(node.right)
        return root
