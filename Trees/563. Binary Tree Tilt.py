# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tilt=[]
        def treesum(node):
            nonlocal tilt
            if not node:
                return 0
            left_sum=treesum(node.left)
            right_sum=treesum(node.right)
            tilt.append(abs(left_sum-right_sum))
            return left_sum + right_sum + node.val
            
        treesum(root)
        return sum(tilt)
