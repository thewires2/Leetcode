class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x=[[-1,0],[0,-1],[1,0],[0,1]]
        count=0
        self.visited={}
        def dfs(r,c):
            key=str(r)+','+str(c)
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]): return 
            if key in self.visited: return 
            self.visited[key]=1
            for i in x:
                r1=r+i[0]
                c1=c+i[1]
                if r1>=0 and r1<len(grid) and c1>=0 and c1<len(grid[0]):
                    if grid[r1][c1]=="1":
                        dfs(r1,c1)  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and str(i)+','+str(j) not in self.visited:
                    dfs(i,j)
                    count+=1
        return count
            
            
