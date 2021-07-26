class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        def getdepth(node):
            depth=0
            while node:
                depth+=1
                node=node.parent
                
            return depth
        
        n,m=map(getdepth,(p,q))
        
        if m>n:
            p,q=q,p
        
        depth_diff=abs(m-n)
        
        while depth_diff:
            p = p.parent
            depth_diff-=1
            
        while p!=q:
            p=p.parent
            q=q.parent
            
        return p
