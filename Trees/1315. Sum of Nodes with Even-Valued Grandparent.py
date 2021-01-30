# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.k=0
        def dfs(root):
            if root:
                if root.val%2==0:
                    if root.left:
                        if root.left.left:
                            self.k+=root.left.left.val
                        if root.left.right:
                            self.k+=root.left.right.val
                    if root.right:
                        if root.right.right:
                            self.k+=root.right.right.val
                        if root.right.left:
                            self.k+=root.right.left.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.k
