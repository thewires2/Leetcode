class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(root,path,k):
            if not root:
                return False
            
            path.append(root)
            
            if root==k:
                return True
            
            if (root.left!=None and find_path(root.left,path,k)) or (root.right!=None and find_path(root.right,path,k)):
                return True
            
            path.pop()
            return False
        
        path1=[]
        path2=[]
        
        if find_path(root,path1,q)==False or find_path(root,path2,p)==False:
            return None
        i=0
        while i<len(path1) and i<len(path2):
            if path1[i]!=path2[i]:
                break
            i+=1
        return path1[i-1]
        
