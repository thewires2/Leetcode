# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.found = None
        x = {}
        stack = [[root,0]]
        k=0
        while stack:
            a = stack.pop()
            if a[0]:
                x[a[0]]=a[1]
                k=max(k,a[1])
                stack.append([a[0].left,a[1]+1])
                stack.append([a[0].right,a[1]+1])

        t=[]
        for key,value in x.items():
            if value==k:
                t.append(key)
        
        def lca(root,t):
            if not root:
                return 0
            
            foundAncestors=lca(root.left,t)+lca(root.right,t)
            
            if root in t:
                foundAncestors+=1
                
            if foundAncestors==len(t):
                self.found=self.found or root
                
            return foundAncestors
        lca(root,t)
        return self.found
        
        return lca(root,p,q)
            
