"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        x=[]
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                x.append(node.val)
                if node.children!=[]:
                    for i in node.children[::-1]:
                        stack.append(i)
                        
                        
        return x
