class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        nums=[0] * (n+1)
        nums[0] = 0
        nums[1] = 1
        for i in range(1,(n+1)//2):
            nums[2*i]=nums[i]
            nums[2 * i + 1] = nums[i] + nums[i + 1]
        return max(nums)
