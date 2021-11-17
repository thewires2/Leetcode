# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def __init__(self):
        self.visited = {}
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        def dfs(root):
            if not root:
                return root
            if root in self.visited:
                return self.visited[root]
            node = NodeCopy(root.val)
            self.visited[root]=node
            node.left = dfs(root.left)
            node.right = dfs(root.right)
            node.random = dfs(root.random)

            return node
        return dfs(root)
