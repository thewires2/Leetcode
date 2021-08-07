class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)-1
        n=len(grid[0])-1
        
        def dp(m,n,memo={}):
            key=str(m)+','+str(n)
            if key in memo: return memo[key]
            if m==0 and n==0: return grid[m][n]
            if m<0 or n<0: return float(inf)
            
            memo[key]=grid[m][n]+min(dp(m-1,n,memo),dp(m,n-1,memo))
            return memo[key]
        return dp(m,n)
        
        
            
            
