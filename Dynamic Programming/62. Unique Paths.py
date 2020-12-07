class Solution:
    def uniquePaths(self, m: int, n: int,memo={}) -> int:
        key=str(m)+','+str(n)
        if key in memo:
            return memo[key]
        if m==1 or n==1:
            return 1
        if m==0 and n==0:
            return 0
        memo[key]=self.uniquePaths(m-1,n,memo)+self.uniquePaths(m,n-1,memo)
        return memo[key]
        
