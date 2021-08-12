# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        
        x = {}
        head=None
        stack = [root]
        
        while stack:
            a = stack.pop()
            if a:
                x[a]=a.val
                if a.right in x and head==None:
                    head=a
                stack.append(a.left)
                stack.append(a.right)
        stack = [root]
        print(head.val)
        while stack:
            a = stack.pop()
            if a:
                if a.right==head:
                    a.right=None
                elif a.left==head:
                    a.left=None
                stack.append(a.left)
                stack.append(a.right)
        return root
                    
