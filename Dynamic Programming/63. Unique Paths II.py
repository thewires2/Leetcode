class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)-1
        n=len(obstacleGrid[0])-1
        
        def grid(m,n,obstacleGrid,memo={}):
            key=str(m)+","+str(n)
            if key in memo: return memo[key]
            if m==0 and n == 0:
                if obstacleGrid[m][n] == 1:
                    return 0
                return 1
            if m<0 or n<0 or obstacleGrid[m][n]==1: return 0
            
            memo[key]= grid(m-1,n,obstacleGrid,memo)+grid(m,n-1,obstacleGrid,memo)
            return memo[key]
        return grid(m,n,obstacleGrid)
