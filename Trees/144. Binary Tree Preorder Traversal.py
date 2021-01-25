# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.x=[]
        def predfs(node):
            if node:
                self.x.append(node.val)
                predfs(node.left)
                predfs(node.right)
        predfs(root)
        return self.x
