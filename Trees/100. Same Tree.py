# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        stack=[(p,q)]
        while stack:
            p,q=stack.pop()
            if p and q:
                if p.val==q.val:
                    stack.append((p.left,q.left))
                    stack.append((p.right,q.right))
                else:
                    return False
            elif p and not q:
                return False
            elif q and not p:
                return False
        return True
