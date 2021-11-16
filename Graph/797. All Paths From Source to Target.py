class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        target = len(graph)-1
        results = []
        
        def backtrack(node,path):
            
            if node == target:
                results.append(list(path))
                return
            
            for nextnode in graph[node]:
                path.append(nextnode)
                backtrack(nextnode,path)
                path.pop()
                
                
        path = deque([0])
        backtrack(0,path)
        
        return results
