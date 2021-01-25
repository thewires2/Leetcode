# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        x=[]
        def dfs(root):
            if root:
                dfs(root.left)
                x.append(root.val)
                dfs(root.right)
        dfs(root)
        node=TreeNode(x[0])
        t=node
        for i in range(1,len(x)):
            temp=TreeNode(x[i])
            node.right=temp
            node.left=None
            node=node.right
        return t
