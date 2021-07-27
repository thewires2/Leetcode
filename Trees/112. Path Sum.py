# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def path(root,remainder,pathnode,pathlist):
            if not root:
                return None
            
            pathnode.append(root.val)
            
            if remainder==root.val and not root.left and not root.right:
                pathlist.append(pathnode)
            else:
                path(root.left,remainder-root.val,pathnode,pathlist)
                path(root.right,remainder-root.val,pathnode,pathlist)
                
            pathnode.pop()
            
        pathnode=[]
        pathlist=[]
            
        path(root,targetSum,pathnode,pathlist)
        return pathlist
            
        
        
        
