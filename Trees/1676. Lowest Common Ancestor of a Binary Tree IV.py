class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.found=None
        
        nodes = set(nodes)
        def traverse(root):
            if not root:
                return 0
            
            foundAncestors = traverse(root.right)+traverse(root.left)
            
            if root in nodes:
                foundAncestors+=1
            
            if foundAncestors == len(nodes):
                self.found=self.found or root
                
            return foundAncestors
                
        traverse(root)
        return self.found
            
        
