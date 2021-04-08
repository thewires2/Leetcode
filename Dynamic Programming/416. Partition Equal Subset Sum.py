class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        x=sum(nums)
        if x%2!=0:
            return False
        k=sum(nums)//2
        dp = [[False] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1,n+1):
            curr=nums[i-1]
            for j in range(k+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-curr] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][k]
