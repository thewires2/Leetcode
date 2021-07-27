# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def path(root,remainingSum,x,paths):
            
            if not root:
                return 
            
            x.append(root.val)
            
            if remainingSum==root.val and not root.left and not root.right:
                paths.append(list(x))
            else:
                path(root.left,remainingSum-root.val,x,paths)
                path(root.right,remainingSum-root.val,x,paths)
            
            x.pop()
        paths=[]
        path(root,targetSum,[],paths)
        return paths
        
