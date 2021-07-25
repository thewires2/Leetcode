# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        x={}
        stack = [[root,0]]
        h=0
        while stack:
            a=stack.pop()
            if a[0]:
                if a[1] not in x:
                    x[a[1]]=[a[0].val]
                else:
                    x[a[1]].append(a[0].val)
                if a[0].left!=None:
                    stack.append([a[0].left,a[1]+1])
                if a[0].right!=None:
                    stack.append([a[0].right,a[1]+1])
        return sum(x[max(x)])
        
                
