class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = {}
        reachable = []
        
        for i in edges:
            if i[1] not in graph:
                graph[i[1]]=[i[0]]
            else:
                graph[i[1]].append(i[0])
                
        
        for i in range(n):
            if i not in graph:
                reachable.append(i)
                
        return reachable
