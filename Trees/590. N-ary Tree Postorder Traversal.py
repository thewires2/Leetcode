"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        x=[]
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                stack.extend(node.children)
                x.append(node.val)
        return x[::-1]
            
