class Solution:
    def minOperations(self, nums: List[int]) -> int:
        k=0
        for i in range(1,len(nums)):
            if nums[i-1]>=nums[i]:
                k+=nums[i-1]-nums[i]+1
                nums[i]+=nums[i-1]-nums[i]+1
        return k
