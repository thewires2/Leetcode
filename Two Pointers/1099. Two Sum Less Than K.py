class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        x=-1
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<k:
                    x=max(x,nums[i]+nums[j])
        return x
