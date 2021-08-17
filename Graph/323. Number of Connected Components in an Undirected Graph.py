class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.visited={}
        def create(edges):
            x={}
            for i in edges:
                if i[0] not in x:
                    x[i[0]]=[]
                if i[1] not in x:
                    x[i[1]]=[]
                x[i[0]].append(i[1])
                x[i[1]].append(i[0])
        
            return x
        
        graph = create(edges)
        print(graph)
        def explore(graph,current):
            if current in self.visited: return False
            self.visited[current]=0
            for i in graph[current]:
                explore(graph,i)
            
            return True
        k=0
        for i in graph:
            if i not in self.visited:
                if explore(graph,i)==True:
                    k+=1
        print(self.visited)
        return k + n -len(self.visited)
