# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        x=[]
        stack=[root]
        while stack:
            root=stack.pop()
            if root:
                if root.left and not root.right:
                    x.append(root.left.val)
                elif root.right and not root.left:
                    x.append(root.right.val)
                stack.append(root.right)
                stack.append(root.left)
        return x
