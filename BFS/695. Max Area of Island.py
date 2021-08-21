class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visited={}
        maxsize=0
        x=[[0,-1],[-1,0],[1,0],[0,1]]
        def exploresize(r,c):
            key=str(r)+','+str(c)
            if key in self.visited: return 0
            self.visited[key]=0
            size=1
            for i in x:
                r1=r+i[0]
                c1=c+i[1]
                if r1>=0 and r1<len(grid) and c1>=0 and c1<len(grid[0]):
                    if grid[r1][c1]==1:
                        size+=exploresize(r1,c1)
            return size
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                f=str(i)+','+str(j)
                if grid[i][j]==1 and f not in self.visited:
                    maxsize=max(maxsize,exploresize(i,j))
        return maxsize
