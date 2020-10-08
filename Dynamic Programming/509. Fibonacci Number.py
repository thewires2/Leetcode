class Solution:
    def fib(self, N: int) -> int:
        if N==0:
            return 0
        if N==1:
            return 1
        dp=[0]*N
        dp[0]=1
        dp[1]=1
        for i in range(2,N):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[N-1]
